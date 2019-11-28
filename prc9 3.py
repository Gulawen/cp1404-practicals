def main():
    numbers= (54,76,32,14,29,12,64,97,50,86,43,12)

    menu_op = menu()

    if menu_op =="1":
        display_minimum(numbers)
    elif menu_op == "2":
        display_maximum(numbers)
    elif menu_op =="3":
        display_total(numbers)
    elif menu_op =="4":
        display_average(numbers)
    elif menu_op =="5":
        return 0
    else:
        main()
    main()

def menu():
    menu_op = input("1 - Display minmum\n2 - Display maximum\n3 - Display total\n4 - Display averge\n5 - Quit\n")
    return menu_op

def display_minimum(numbers):
    min = numbers[0]
    for n in numbers :
        if n<min:
            min = n
    print("The minimum number in this tuple is %d\n"%min)

def display_maximum(numbers):
    max = numbers[0]
    for n in numbers:
        if n >max:
            max = n
    print("The maximum number in this tuple is %d\n"%max)

def display_total(numbers):
    total = 0
    for n in numbers:
        total = n +total
    print("The total of this tuple is %d\n"%total)

def display_average(numbers):
    total = 0
    for n in numbers:
        total = n + total
        avg = total/12
    print("The average of this tuple is %d\n"%avg)
main()