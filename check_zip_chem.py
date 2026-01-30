import zipfile
import os

def list_zip():
    zip_path = "download/ToxValDB_v9.7.0_Release.zip"
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for f in zip_ref.namelist():
            if "chemical" in f.lower() or "smiles" in f.lower() or "structure" in f.lower():
                print(f)

if __name__ == "__main__":
    list_zip()
