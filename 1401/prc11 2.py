def main():
    try:
        ages = int(input('Please enter your age : '))
        if ages < 1 or ages > 100:
            print("Invalid input!")
            main()
        else:
            print("Thx for input")

    except:
        print("invalid input!")
        main()
main()


