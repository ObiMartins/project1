# analyzer.py
import pandas as pd
from helpers import calculate_total, format_currency, calculate_discount

# Read data
try:
    data_frame = pd.read_csv("data/sales.csv")
    # Calculate total for each row

    required_columns = ["product", "quantity", "price"]
    for col in required_columns:
        if col not in data_frame.columns:
            raise KeyError(f"Missing required column: {col}")
    
except FileNotFoundError as e:
    print("Error: The file 'sales.csv' was not found in the 'data' directory. {e}" )
    exit(1)

totals = []
try:
    for index, row in data_frame.iterrows():
        total = calculate_total(row["quantity"], row["price"])
        totals.append(total)
    data_frame["total"] = totals
except (ValueError, TypeError) as e:
        print(f"Error calculating total for row {index}: {e}")
        
except pd.errors.EmptyDataError:
    print("sales.csv file is empty")

except pd.errors.ParserError:
    print("CSV file format is invalid")

except KeyError as e:
    print("Missing required column in CSV file:", e)

except Exception as e:
    print("An unexpected error occurred:", e)

    for index, row in data_frame.iterrows():
        formatted_total = format_currency(row["total"])
        print(f"{row['product']}: {formatted_total}")
    

# Show grand total
grand_total = data_frame["total"].sum()
# formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {grand_total}")

# Calculate Discount for Grand Total
discount_price = calculate_discount(grand_total, 10)
print(f"\nDiscount amount for Total price is : N{discount_price:.2f}")
payable_amount = grand_total - discount_price
print(f"\nPayable amount after discount is : N{payable_amount:.2f}")