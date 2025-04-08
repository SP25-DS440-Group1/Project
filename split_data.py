import pandas as pd
from pathlib import Path

# Input merged dataset file
MERGED_FILE = "./Datasets/Weather_Datasets/merged_dataset.csv"  # Replace with your merged dataset path
OUTPUT_DIR = "./Datasets/Weather_Datasets/Split_Data/"              # Where to save train/val/test sets
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Load the full dataset
df = pd.read_csv(MERGED_FILE, parse_dates=["timestamp"])

# Sort by time for chronological splitting
df.sort_values(by="timestamp", inplace=True)

# Determine split sizes (80/10/10)
n_total = len(df)
n_train = int(n_total * 0.8)
n_val = int(n_total * 0.1)
n_test = n_total - n_train - n_val

# Split the dataset
df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train + n_val]
df_test = df.iloc[n_train + n_val:]

# Save to CSV files
df_train.to_csv(f"{OUTPUT_DIR}/train.csv", index=False)
df_val.to_csv(f"{OUTPUT_DIR}/val.csv", index=False)
df_test.to_csv(f"{OUTPUT_DIR}/test.csv", index=False)

print("✅ Training/Validation/Test splits saved:")
print(f"  Train: {len(df_train)} rows")
print(f"  Val:   {len(df_val)} rows")
print(f"  Test:  {len(df_test)} rows")
