def main():
    age = int(input("please enter your age:"))
    if age < 0 or age > 130:
        print("That age is invalid")
        main()
    else :
        print("Age accepted. Have a nice day")
main()

