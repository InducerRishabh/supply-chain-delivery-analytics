from pathlib import Path
import sys
import duckdb


# --------------------------------------------------
# Project paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "DataCoSupplyChain_UTF8.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# Select SQL file
# --------------------------------------------------

if len(sys.argv) != 2:
    print(
        "Usage: python src/run_sql.py "
        "sql/query_file.sql"
    )
    sys.exit(1)


sql_file = PROJECT_ROOT / sys.argv[1]

if not sql_file.exists():
    print(f"SQL file not found: {sql_file}")
    sys.exit(1)


# --------------------------------------------------
# Read SQL
# --------------------------------------------------

sql = sql_file.read_text(encoding="utf-8")

sql = sql.replace(
    "'data/DataCoSupplyChain_UTF8.csv'",
    f"'{DATA_FILE.as_posix()}'"
)


# --------------------------------------------------
# Execute query
# --------------------------------------------------

result = duckdb.sql(sql).df()


# --------------------------------------------------
# Save result
# --------------------------------------------------

output_file = (
    OUTPUT_DIR
    / f"{sql_file.stem}.csv"
)

result.to_csv(
    output_file,
    index=False
)


# --------------------------------------------------
# Display result
# --------------------------------------------------

print("\n" + "=" * 80)
print(sql_file.name.upper())
print("=" * 80)

print(result.to_string(index=False))

print()
print(f"Saved result to: {output_file}")