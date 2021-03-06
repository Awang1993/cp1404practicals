"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    i = int(input("How many months? "))
    number_of_months = i

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(str(month))))
        incomes.append(income)

    generate_income_report(number_of_months, incomes)


def generate_income_report(number_of_months, incomes):
    """Generates income report from user input and formats output string"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:>10.2f}  \t \tTotal: ${:>10.2f}".format(month, income, total))


main()