from pathlib import Path
import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

csv_file = next(DATA_DIR.glob("*.csv"))

print(f"Loading: {csv_file.name}")

df = pd.read_csv(csv_file, encoding="latin1")


# --------------------------------------------------
# Create our independently derived shipping delay
# --------------------------------------------------

df["shipping_delay_days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

df["derived_late"] = (
    df["shipping_delay_days"] > 0
).astype(int)


# --------------------------------------------------
# 1. Shipping delay distribution
# --------------------------------------------------

print("\n" + "=" * 60)
print("SHIPPING DELAY DISTRIBUTION")
print("=" * 60)

print(
    df["shipping_delay_days"]
    .value_counts()
    .sort_index()
)


# --------------------------------------------------
# 2. Compare our derived flag with dataset flag
# --------------------------------------------------

print("\n" + "=" * 60)
print("DERIVED LATE VS DATASET LATE FLAG")
print("=" * 60)

comparison = pd.crosstab(
    df["derived_late"],
    df["Late_delivery_risk"],
    margins=True
)

print(comparison)


# --------------------------------------------------
# 3. Agreement rate
# --------------------------------------------------

agreement = (
    df["derived_late"]
    == df["Late_delivery_risk"]
).mean()

print("\n" + "=" * 60)
print("AGREEMENT RATE")
print("=" * 60)

print(f"{agreement:.2%}")


# --------------------------------------------------
# 4. Compare delivery status
# --------------------------------------------------

print("\n" + "=" * 60)
print("DELIVERY STATUS")
print("=" * 60)

print(
    pd.crosstab(
        df["Delivery Status"],
        df["derived_late"],
        margins=True
    )
)


# --------------------------------------------------
# 5. Overall metrics
# --------------------------------------------------

print("\n" + "=" * 60)
print("OVERALL DELIVERY METRICS")
print("=" * 60)

print(
    f"Average actual shipping days: "
    f"{df['Days for shipping (real)'].mean():.2f}"
)

print(
    f"Average scheduled shipping days: "
    f"{df['Days for shipment (scheduled)'].mean():.2f}"
)

print(
    f"Average shipping delay: "
    f"{df['shipping_delay_days'].mean():.2f}"
)

print(
    f"Derived late rate: "
    f"{df['derived_late'].mean():.2%}"
)

print(
    f"Dataset late-risk rate: "
    f"{df['Late_delivery_risk'].mean():.2%}"
)