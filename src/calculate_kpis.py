from pathlib import Path
import pandas as pd


# --------------------------------------------------
# 1. Load data
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

csv_file = next(DATA_DIR.glob("*.csv"))

df = pd.read_csv(csv_file, encoding="latin1")


# --------------------------------------------------
# 2. Create shipping-delay metric
# --------------------------------------------------

df["shipping_delay_days"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)


# --------------------------------------------------
# 3. Define delivery-performance population
# --------------------------------------------------

valid_delivery_statuses = [
    "Advance shipping",
    "Late delivery",
    "Shipping on time"
]

delivery_df = df[
    df["Delivery Status"].isin(valid_delivery_statuses)
].copy()


# --------------------------------------------------
# 4. Calculate order counts
# --------------------------------------------------

total_records = len(df)

delivery_records = len(delivery_df)

cancelled_records = (
    df["Delivery Status"] == "Shipping canceled"
).sum()

late_orders = (
    delivery_df["Delivery Status"] == "Late delivery"
).sum()

on_time_orders = (
    delivery_df["Delivery Status"] == "Shipping on time"
).sum()

advance_orders = (
    delivery_df["Delivery Status"] == "Advance shipping"
).sum()


# --------------------------------------------------
# 5. Calculate delivery KPIs
# --------------------------------------------------

late_delivery_rate = (
    late_orders / delivery_records
)

on_time_or_early_rate = (
    (on_time_orders + advance_orders)
    / delivery_records
)

cancellation_rate = (
    cancelled_records / total_records
)

average_shipping_delay = (
    delivery_df["shipping_delay_days"].mean()
)


# --------------------------------------------------
# 6. Display results
# --------------------------------------------------

print("\n" + "=" * 60)
print("SUPPLY CHAIN DELIVERY KPIs")
print("=" * 60)

print(f"Total records:              {total_records:,}")
print(f"Delivery records:           {delivery_records:,}")
print(f"Cancelled records:          {cancelled_records:,}")
print()

print(f"Late deliveries:            {late_orders:,}")
print(f"On-time deliveries:         {on_time_orders:,}")
print(f"Advance deliveries:         {advance_orders:,}")
print()

print(f"Late delivery rate:         {late_delivery_rate:.2%}")
print(f"On-time / early rate:       {on_time_or_early_rate:.2%}")
print(f"Cancellation rate:          {cancellation_rate:.2%}")
print(f"Average shipping delay:     {average_shipping_delay:.2f} days")