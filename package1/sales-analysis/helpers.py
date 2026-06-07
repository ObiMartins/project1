# helpers.py
def calculate_total(quantity, price):
#Calculate total for a single item.
    return quantity * price



def format_currency(amount):
#Format number as currency."""
    return f"N{amount:,.2f}"

def calculate_discount(amount, percent):
    return amount * percent / 100

def apply_discount(amount, percent):
    # Calculate final amount after discount
    discount = calculate_discount(amount, percent)
    return amount - discount
