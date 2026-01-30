import pyarrow.parquet as pq

def check_schema():
    pf = pq.ParquetFile("brick/toxvaldb.parquet")
    print(pf.schema)
    print(f"Num rows: {pf.metadata.num_rows}")

if __name__ == "__main__":
    check_schema()
