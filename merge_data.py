import os
import pandas as pd
from pathlib import Path

# Path to cleaned per-station CSVs (output from the previous script)
CLEANED_DIR = "./Datasets/Weather_Datasets/2024_Clean/"  # Replace with your path
MERGED_FILE = "./Datasets/Weather_Datasets/2024_merged.csv"  # Final merged graph dataset

# Ensure output folder exists
Path(os.path.dirname(MERGED_FILE)).mkdir(parents=True, exist_ok=True)

# Collect all cleaned CSVs
all_dataframes = []
for file in os.listdir(CLEANED_DIR):
    if file.endswith(".csv"):
        file_path = os.path.join(CLEANED_DIR, file)
        try:
            df = pd.read_csv(file_path, parse_dates=["timestamp"])
            all_dataframes.append(df)
            print(f"✅ Loaded: {file}")
        except Exception as e:
            print(f"❌ Failed to load {file}: {e}")

# Merge all into a single DataFrame
if all_dataframes:
    df_merged = pd.concat(all_dataframes, ignore_index=True)
    df_merged.sort_values(by=["timestamp", "station_id"], inplace=True)
    df_merged.to_csv(MERGED_FILE, index=False)
    print(f"✅ Merged dataset saved to: {MERGED_FILE}")
else:
    print("⚠️ No valid CSVs were found to merge.")
