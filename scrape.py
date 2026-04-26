import requests
import os
import zipfile

# Base directories
BASE_DIR = "C:/Users/DS/Documents/cricketsheet/data"
DOWNLOAD_DIR = os.path.join(BASE_DIR, "raw_json")
ZIP_DIR = os.path.join(BASE_DIR, "zips")

# Create main folders
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(ZIP_DIR, exist_ok=True)

# Dataset URLs
urls = {
    "odi": "https://cricsheet.org/downloads/odis_json.zip",
    "t20": "https://cricsheet.org/downloads/t20s_json.zip",
    "test": "https://cricsheet.org/downloads/tests_json.zip",
    "ipl": "https://cricsheet.org/downloads/ipl_json.zip"
}

for name, url in urls.items():
    print(f"\n📥 Downloading {name.upper()} data...")

    # Step 1: Download ZIP
    zip_path = os.path.join(ZIP_DIR, f"{name}.zip")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Failed to download {name}")
        continue

    with open(zip_path, "wb") as f:
        f.write(response.content)

    print(f"✅ Downloaded: {zip_path}")

    # Step 2: Create separate folder for each format
    format_folder = os.path.join(DOWNLOAD_DIR, name)
    os.makedirs(format_folder, exist_ok=True)

    # Step 3: Extract ZIP into that folder ONLY
    print(f"📂 Extracting {name.upper()} files...")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(format_folder)

    print(f"✅ Extracted to: {format_folder}")

print("\n🎉 All datasets downloaded and organized successfully!")