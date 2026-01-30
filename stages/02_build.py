import os
import glob
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def build_brick():
    input_dir = "download/Data Excel Files"
    output_dir = "brick"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "toxvaldb.parquet")
    
    # Pattern for data files
    files = glob.glob(os.path.join(input_dir, "toxval_all_*.xlsx"))
    files.sort()
    
    if not files:
        print("No data files found to process.")
        return

    print(f"Found {len(files)} files to process.")
    
    # Initialize ParquetWriter with the schema from the first file
    writer = None
    
    for i, file_path in enumerate(files):
        print(f"Processing {i+1}/{len(files)}: {os.path.basename(file_path)}")
        try:
            # Read Excel
            # Ensure identifiers are strings to avoid mix of int/str
            df = pd.read_excel(file_path, dtype={
                'DTXSID': str, 
                'CASRN': str, 
                'TOXVAL_NUMERIC': float,
                'YEAR': str, # Year can be mixed
                'QC_STATUS': str
            })
            
            # Standardize columns? They seemed consistent in check.
            # Convert to pyarrow table
            table = pa.Table.from_pandas(df)
            
            if writer is None:
                writer = pq.ParquetWriter(output_file, table.schema)
            else:
                # Ensure schema compatibility
                if table.schema != writer.schema:
                    # If schema mismatch (e.g. column order or type), cast to writer schema
                    # This handles slight variations or missing columns if any
                    # But checking earlier showed they matched.
                    # Just in case, we align columns
                    try:
                        table = table.cast(writer.schema)
                    except Exception as e:
                        print(f"Schema mismatch for {file_path}: {e}")
                        # Attempt to fix by reordering columns or filling missing
                        # This is complex, hopefully not needed.
                        # We can try to align by name
                        # create a new table with same columns as writer
                        common_cols = [c.name for c in writer.schema]
                        # Add missing columns as null
                        for col in common_cols:
                            if col not in df.columns:
                                df[col] = None
                        # Drop extra columns
                        df = df[common_cols]
                        table = pa.Table.from_pandas(df, schema=writer.schema)

            writer.write_table(table)
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    if writer:
        writer.close()
        print(f"Written to {output_file}")
    else:
        print("No data written.")

if __name__ == "__main__":
    build_brick()
