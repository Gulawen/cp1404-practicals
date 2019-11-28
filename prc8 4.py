# The calc_discount_price function accepts an item’s price
# and the discount percentage as arguments. It uses those
# values to calculate and return the discounted price.

def main():
    # Calculate the discount.
    price = float(input("pls enter the price:"))
    percentage = float(input("pls enter the percentage:"))
    calc_discount_price(price, percentage)
    print("The discount price is", calc_discount_price(price, percentage))

def calc_discount_price(price, percentage):
    discount = price * percentage
    discountPrice = price - discount
    return discountPrice
main()