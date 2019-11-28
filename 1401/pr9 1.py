
def main():
    num1 = int(input("please enter the number1"))
    num2 = int(input("please enter the number2"))
    num3 = int(input("please enter the number3"))
    num4 = int(input("please enter the number4"))
    num5 = int(input("please enter the number5"))
    list = [num1, num2, num3, num4, num5]
    result_list =sorted(list, reverse=True)
    for x in result_list:
        print(x)
    result_list2 = sorted(list, reverse=False)
    for x in result_list2:
        print(x)
main()