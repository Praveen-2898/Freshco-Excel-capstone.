# analysis.py
# Reproduce the summaries used in the Excel workbook for Freshco Hyper Market Capstone (sample data)
import pandas as pd

df = pd.read_csv("data_raw_freshco.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

monthly = df.groupby("month", sort=True)["total_price"].sum().reset_index().rename(columns={"total_price":"revenue"})
category_sales = df.groupby("category")["total_price"].sum().reset_index().sort_values("total_price", ascending=False).rename(columns={"total_price":"revenue"})
payment_summary = df.groupby("payment_method").agg(orders=("order_id","count"), revenue=("total_price","sum")).reset_index().sort_values("revenue", ascending=False)

print("Monthly revenue (top rows):")
print(monthly.head())

print("\nTop categories:")
print(category_sales.head())

print("\nPayment method summary:")
print(payment_summary.head())

# To create an Excel file with the same tables, run:
#   python analysis.py
# and use pandas.ExcelWriter to write the dataframes to sheets.
