def main():
    MAX_SETS = 5
    MAX_NUMBERS = 2

    sum = 0
    total = 0

    for set in range(MAX_SETS):
        for number in range(MAX_NUMBERS):
            value = int(input("Enter number " + str(number) + " of set " + str(set) + " : "))
            sum = sum + value
        print("The sum of set", set, "is", sum, ".")
        total = total + sum
        sum = 0

    print("The total of all the sets is ", total, ".")
main()