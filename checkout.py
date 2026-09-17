# checkout.py
def calculate_total(price, tax):
    total = price + (price * tax)
    #return total # Notable modification
    return round(total) # Modified calculation
# Added calculation function for discounts
def apply_discount(price, discount):
    return price - discount

