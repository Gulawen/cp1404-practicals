def main():
    item1 =  int(input("Please enter the number of the item:"))
    total_price = 0

    while item1< 0:
        print("Invalid ")
        item1 = int(input("Please enter the number of the item:"))
    for i in range(item1):
        price = float(input("Please enter the price of the item:"))
        total_price = total_price + price
    if total_price >= 100:
        total_price= total_price *0.9
    print("The total price for" + str(item1)+ "is " +str(total_price))
main()