def main():
    my_string = input("Please enter something here, can be numbers,text or punctuation. : ")

    count_digit = 0
    count_letters = 0

    for i in my_string:
        if i.isdigit():
            count_digit = count_digit + 1
        elif i.lower().islower():
            count_letters = count_letters + 1
    print("Letter :" + str(count_letters)+" Digits : "+ str(count_digit ))
main()