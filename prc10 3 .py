def main():
    password = input("Please enter password (must have one lower,one upper,one numerical and one special letter.)")
    one = validate_password(password)

    if one == 'false':
        print("Invalid password please try again")
        main()
    else:
        print("You input is accepted!")

def validate_password(password):
    onelower = 'false'
    oneupper = 'false'
    onedigit = 'false'
    onespecial = 'false'
    oneletters = [',', '.', '@', '#', '!', '$', '%', '^', '&', '*']
    for i in password:
        if i.islower():
            onelower = 'true'
        elif i.isupper():
            oneupper = 'true'
        elif i.isdigit():
            onedigit = 'true'
        elif i in oneletters:
            onespecial = 'true'
    if onedigit == 'true' and onelower == 'true' and onespecial == 'true' and oneupper == 'true':
        return 'true'
    else:
        return 'false'


main()
