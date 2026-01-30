import os
import json
import pyarrow.parquet as pq

def test():
    print("Running brick tests...")
    
    # Check files
    required_files = [
        "dvc.yaml",
        "dvc.lock",
        ".bb/brick.jsonld",
        ".bb/provenance.jsonld",
        ".bb/datapackage.json",
        "brick/toxvaldb.parquet"
    ]
    
    for f in required_files:
        if not os.path.exists(f):
            print(f"Error: Missing {f}")
            exit(1)
            
    # Validate Parquet
    try:
        pf = pq.ParquetFile("brick/toxvaldb.parquet")
        if pf.metadata.num_rows == 0:
            print("Error: Parquet file is empty")
            exit(1)
        print(f"Parquet file valid. Rows: {pf.metadata.num_rows}")
    except Exception as e:
        print(f"Error reading Parquet: {e}")
        exit(1)
        
    print("All tests passed.")

if __name__ == "__main__":
    test()
