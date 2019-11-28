def main():
    print("Welcome to the Salary Calculator")
    name = input("Please enter your name: ")
    while name == "":#check if there is no enter
        print("Name must be at least 1 character")
        name = input("Please enter your name: ")
    salary= int(input("Please enter your beginning salary:"))
    while salary < 10000:# check if it is the condition of salary<10000
        print("Sorry, your beginning salary must be at least 10000")
        salary = int(input("Please enter your beginning salary:"))
    yw = int(input("Please enter the years worked:"))
    while yw < 1 or yw > 10:#check the condition of yw<1 or yw>10
        print("Years worked must be at least 1, maximum of 10")
        yw = int(input("Please enter the years worked:"))
    for i in range(yw):#use the loop to print out every year salary
        print("year" + str(i + 1) + ":" + str(salary))
        salary = salary * 1.02
main()