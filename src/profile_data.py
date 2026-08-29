from pathlib import Path
import pandas as pd


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

csv_files = list(DATA_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError("No CSV file found in the data folder.")

if len(csv_files) > 1:
    raise ValueError(f"Expected one CSV file, found: {csv_files}")

DATA_FILE = csv_files[0]

print(f"Loading: {DATA_FILE.name}")


# --------------------------------------------------
# Load dataset
# --------------------------------------------------

df = pd.read_csv(DATA_FILE, encoding="latin1")


# --------------------------------------------------
# 1. Dataset overview
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")


# --------------------------------------------------
# 2. Column names
# --------------------------------------------------

print("\n" + "=" * 60)
print("COLUMNS")
print("=" * 60)

for column in df.columns:
    print(column)


# --------------------------------------------------
# 3. Data types
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)


# --------------------------------------------------
# 4. Missing values
# --------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = df.isna().sum().sort_values(ascending=False)
missing = missing[missing > 0]

if missing.empty:
    print("No missing values found.")
else:
    print(missing)


# --------------------------------------------------
# 5. Duplicate rows
# --------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATES")
print("=" * 60)

print(f"Duplicate rows: {df.duplicated().sum():,}")


# --------------------------------------------------
# 6. Numerical summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("NUMERICAL SUMMARY")
print("=" * 60)

print(df.describe().T)


# --------------------------------------------------
# 7. Categorical columns
# --------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORICAL COLUMNS")
print("=" * 60)

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:
    print(
        f"{column}: "
        f"{df[column].nunique(dropna=True):,} unique values"
    )


# --------------------------------------------------
# 8. Delivery-related columns
# --------------------------------------------------

print("\n" + "=" * 60)
print("DELIVERY-RELATED COLUMNS")
print("=" * 60)

delivery_keywords = [
    "ship",
    "delivery",
    "late",
    "days"
]

delivery_columns = [
    column
    for column in df.columns
    if any(
        keyword in column.lower()
        for keyword in delivery_keywords
    )
]

for column in delivery_columns:
    print(column)


# --------------------------------------------------
# 9. Geographic / market columns
# --------------------------------------------------

print("\n" + "=" * 60)
print("GEOGRAPHIC / MARKET COLUMNS")
print("=" * 60)

geo_keywords = [
    "region",
    "market",
    "country",
    "state",
    "city"
]

geo_columns = [
    column
    for column in df.columns
    if any(
        keyword in column.lower()
        for keyword in geo_keywords
    )
]

for column in geo_columns:
    print(column)


# --------------------------------------------------
# 10. Sample records
# --------------------------------------------------

print("\n" + "=" * 60)
print("SAMPLE RECORDS")
print("=" * 60)

print(df.head())