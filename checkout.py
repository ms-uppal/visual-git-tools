# checkout.py
def calculate_total(price, tax):
    return price + (price * tax)

print("Total price is:", calculate_total(100, 0.06))
