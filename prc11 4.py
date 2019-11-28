def main():
    file_name = input("Please enter the file name you want to use : ")

    user_name = input("Please enter your name : ")

    user_age = input("Please enter your age : ")

    user_address = input("Please enter your address : ")

    f = open(file_name, 'w')

    f.write(str(user_name), str(user_age), str(user_address))

    f.close()

    F = open(file_name, 'r')

    print(F.read())
main()