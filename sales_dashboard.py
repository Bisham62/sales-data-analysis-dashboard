import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print(df.head())

df["Date"] = pd.to_datetime(df["Date"])
df["Units_Sold"] = df["Units_Sold"].fillna(df["Units_Sold"].mean())
df["Price"] = df["Price"].fillna(df["Price"].mean())

df["Revenue"] = df["Units_Sold"] * df["Price"] * (1 - df["Discount"])
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue: {total_revenue}")

df["Month"] = df["Date"].dt.month_name()

monthly_revenue = df.groupby("Month")["Revenue"].sum()
region_revenue = df.groupby("Region")["Revenue"].sum()
product_revenue = df.groupby("Product")["Revenue"].sum()

month_order = ["January", "February", "March", "April"]
monthly_revenue = monthly_revenue.reindex(month_order)

print("\nMonthly Revenue:")
print(monthly_revenue)

print("\n--- BUSINESS INSIGHTS ---")

best_month = monthly_revenue.idxmax()
print(f"Best performing month: {best_month}")

worst_month = monthly_revenue.idxmin()
print(f"Worst performing month: {worst_month}")

top_product = df.groupby("Product")["Revenue"].sum().idxmax()
print(f"Top selling product: {top_product}")

best_region = df.groupby("Region")["Revenue"].sum().idxmax()
print(f"Best performing region: {best_region}")


print("\n--- RECOMMENDATIONS ---")

print(f"- Focus more on {best_month} since it generates highest revenue")
print(f"- Improve strategies in {worst_month} to boost performance")
print(f"- Promote {top_product} as it is the best-selling product")
print(f"- Expand operations in {best_region} for higher growth")

plt.figure()

monthly_revenue.plot(kind="bar")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

for i, value in enumerate(monthly_revenue):
    plt.text(i, value, f"{int(value)}", ha='center', va='bottom')

best_value = monthly_revenue.max()

plt.text(
    list(monthly_revenue.index).index(best_month),
    best_value,
    f"Best: {best_month}",
    ha='center',
    va='bottom',
    color='red'
)

plt.tight_layout()
plt.show()


plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")

for i, value in enumerate(region_revenue):
    plt.text(i, value, f"{int(value)}", ha='center', va='bottom')

plt.tight_layout()
plt.show()


plt.figure()
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")

for i, value in enumerate(product_revenue):
    plt.text(i, value, f"{int(value)}", ha='center', va='bottom')

plt.tight_layout()
plt.show()
