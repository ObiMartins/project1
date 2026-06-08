# analyzer.py
import pandas as pd
from helpers import calculate_total, format_currency, calculate_discount

# Read data
data_frame = pd.read_csv("data/sales.csv")
# Calculate total for each row

totals = []

for index, row in data_frame.iterrows():
    total = calculate_total(row["quantity"], row["price"])

    totals.append(total)
data_frame["total"] = totals


# Display formatted totals
print("Sales Data:")
for index, row in data_frame.iterrows():
    formatted_total = format_currency(row["total"])
    print(f"{row['product']}: {formatted_total}")
    

# Show grand total
grand_total = data_frame["total"].sum()
#formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {grand_total}")

# Calculate Discount for Grand Total
discount_price = calculate_discount(grand_total, 10)
print(f"\nDiscount amount for Total price is : N{discount_price:.2f}")
payable_amount = grand_total - discount_price
print(f"\nPayable amount after discount is : N{payable_amount:.2f}")