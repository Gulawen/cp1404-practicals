def main():
    x = int(input("please enter the x"))
    y = int(input("please enter the y"))
    doMath(x, y)

    distance = 500
    fuel_rate = 8

    fuel = get_fuel(distance, fuel_rate)
    print("fuel_needed is", fuel)

    stock = int(input("enter stock at start of day"))
    new_stock = int(input("enter amount of new stock received today"))
    sold = int(input("enter amount of stock sold"))
    print("stock amount at end of the day"+ stock, new_stock, sold)
    price = float(input("enter the product price"))
    print(calc_dicount(price))

def doMath(lhs, rhs):
    sum = lhs + rhs
    diff = lhs - rhs
    product = lhs * rhs
    quotient = lhs / rhs
    print("sum" +str(sum))
    print("diff" + str(diff))
    print("product" + str(product))
    print("quotient" + str(quotient))

def get_fuel(distance, consumption):
    fuel_needed = distance * consumption / 100
    return fuel_needed

def format_currency(num):
    return "%.2f" % num
def CXK():
    HOURLY_RATE = 24.95
    noh = int(input("please enter the number of hours worked"))
    return noh*HOURLY_RATE
def calc_dicount(price):
    return format_currency(price*0.8)
main()
