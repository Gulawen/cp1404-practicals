
def main():
    s = input("Enter the string:").lower().replace(" ", "").replace(",", "")
    z = s[:: -1]

    if  s == z :
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


main()