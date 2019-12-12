


def main():
    incomes = []
    total_months = int(input("How many months? "))
    for month in range(1, total_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)
    print_income(incomes)
def print_income(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month+1, income, total))

main()
