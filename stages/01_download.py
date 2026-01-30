import os
import subprocess
import zipfile
import sys

def main():
    url = "https://zenodo.org/records/17088058/files/ToxValDB%20v97_0%20Release.zip?download=1"
    download_dir = "download"
    zip_path = os.path.join(download_dir, "ToxValDB_v9.7.0_Release.zip")
    
    os.makedirs(download_dir, exist_ok=True)
    
    if not os.path.exists(zip_path):
        print(f"Downloading {url}...")
        # Use curl for reliability and speed
        cmd = ["curl", "-L", "-o", zip_path, url]
        ret = subprocess.call(cmd)
        if ret != 0:
            print("Download failed.")
            sys.exit(1)
    else:
        print("File exists, skipping download.")

    print("Inspecting zip file...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            print(f"Zip contains {len(file_list)} files.")
            
            # Identify files to extract
            to_extract = []
            for f in file_list:
                if f.endswith('.xlsx') or f.endswith('.csv') or f.endswith('.txt'):
                    if "__MACOSX" not in f: # Skip mac metadata
                        to_extract.append(f)
            
            print(f"Found {len(to_extract)} relevant files (xlsx/csv/txt).")
            for f in to_extract:
                print(f"Extracting: {f}")
                zip_ref.extract(f, download_dir)
                
    except zipfile.BadZipFile:
        print("Error: Bad Zip File")
        sys.exit(1)
        
    print("Done.")

if __name__ == "__main__":
    main()
