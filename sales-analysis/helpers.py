
def calculate_total(quantity, price):
    """Calculate total for a single item."""
    return quantity * price


def format_currency(amount):
    """Format number as currency of your choice."""
    return f"N{amount:,.2f}"

def calculate_discount(price, discount):
    return price * discount / 100 
