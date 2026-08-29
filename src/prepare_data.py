from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "DataCoSupplyChainDataset.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "DataCoSupplyChain_UTF8.csv"
)


print(f"Reading: {RAW_FILE.name}")

df = pd.read_csv(
    RAW_FILE,
    encoding="latin1"
)

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

print(f"\nCreated: {OUTPUT_FILE.name}")
print("Encoding converted: latin1 → UTF-8")