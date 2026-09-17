# checkout.py - Basic checkout tool
def calculate_total(price, tax):
    """Calculates the final cost including sales tax."""
    return price + (price * tax)

print("Total price is:", calculate_total(100, 0.06))
