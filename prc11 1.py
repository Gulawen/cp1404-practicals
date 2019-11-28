def main():
    try:
        salary = int(input('How much is Your salary? :'))
        salary = salary * (1 + 0.045)
        print("After raise,your salary is "+ str(salary))
    except:
        print('Invalid Input.')
main()