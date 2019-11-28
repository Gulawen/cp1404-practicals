def main():
    age = int(input("Enter your age"))
    enrolled = input("Are you enrolled to vote(Y/N)? ").upper()

    if age >= 18 and enrolled:
        print("you may vote")
    elif age >=18 and not enrolled:
        print("you are not eligible to vote")
    else:
        print("you are not eligible to vote")
main()