import os
import pandas as pd

def check_headers():
    data_dir = "download/Data Excel Files"
    files = [f for f in os.listdir(data_dir) if f.startswith('toxval_all_') and f.endswith('.xlsx')]
    print(f"Found {len(files)} data files.")
    
    if not files:
        print("No data files found!")
        return

    first_headers = None
    for i, f in enumerate(files[:5]):
        path = os.path.join(data_dir, f)
        print(f"Reading {f}...")
        try:
            df = pd.read_excel(path, nrows=0)
            headers = list(df.columns)
            if first_headers is None:
                first_headers = headers
                print(f"Headers ({len(headers)}): {headers}")
            else:
                if headers == first_headers:
                    print("  Headers match.")
                else:
                    print("  Headers DO NOT match.")
                    # print diff
                    set1 = set(first_headers)
                    set2 = set(headers)
                    print(f"  Only in first: {set1 - set2}")
                    print(f"  Only in current: {set2 - set1}")
        except Exception as e:
            print(f"Error reading {f}: {e}")

if __name__ == "__main__":
    check_headers()
