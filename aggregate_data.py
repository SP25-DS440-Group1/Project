import os
import pandas as pd
#from datetime import datetime
from pathlib import Path

# Directory with your per-station CSVs
INPUT_DIR = "./Datasets/Weather_Datasets/2024/"
OUTPUT_DIR = "./Datasets/Weather_Datasets/2024_Clean/"
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Weather parsing helpers
def parse_temp(temp_str):
    try:
        return int(temp_str.split(",")[0]) / 10.0
    except:
        return None

def parse_wind_speed(wnd_str):
    try:
        return int(wnd_str.split(",")[3])  # speed in m/s
    except:
        return None

def parse_visibility(vis_str):
    try:
        return int(vis_str.split(",")[0]) / 10.0
    except:
        return None

def parse_pressure(slp_str):
    try:
        return int(slp_str.split(",")[0]) / 10.0
    except:
        return None

def parse_ceiling(cig_str):
    try:
        return float(cig_str.split(",")[0])
    except:
        return None

# Core processing function for one file
def process_station_csv(filepath):
    station_id = os.path.splitext(os.path.basename(filepath))[0]

    use_cols = ["DATE", "LATITUDE", "LONGITUDE", "TMP", "DEW", "WND", "VIS", "SLP", "CIG"]

    try:
        df = pd.read_csv(filepath, usecols=use_cols, low_memory=False)
        df["timestamp"] = pd.to_datetime(df["DATE"], errors='coerce').dt.floor("H")
        df["station_id"] = station_id

        # Parse and clean numeric weather data
        df["temperature"] = df["TMP"].apply(parse_temp)
        df["dew_point"] = df["DEW"].apply(parse_temp)
        df["wind_speed"] = df["WND"].apply(parse_wind_speed)
        df["visibility"] = df["VIS"].apply(parse_visibility)
        df["pressure"] = df["SLP"].apply(parse_pressure)
        df["ceiling"] = df["CIG"].apply(parse_ceiling)

        # Select final columns
        df_clean = df[[
            "station_id", "timestamp", "LATITUDE", "LONGITUDE",
            "temperature", "dew_point", "wind_speed",
            "visibility", "pressure", "ceiling"
        ]].dropna()

        # Save to output folder
        output_path = os.path.join(OUTPUT_DIR, f"{station_id}_clean.csv")
        df_clean.to_csv(output_path, index=False)
        print(f"✅ Saved cleaned data for station: {station_id}")

    except Exception as e:
        print(f"❌ Failed to process {filepath}: {e}")

# Main loop through all CSVs
if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]
    for file in files:
        full_path = os.path.join(INPUT_DIR, file)
        process_station_csv(full_path)