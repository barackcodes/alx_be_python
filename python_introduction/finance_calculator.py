income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

savings_monthly = income - expenses
savings_yearly = savings_monthly * 12
interest_rate = 0.05
savings_with_interest = savings_yearly * (1 + interest_rate)

print("Your monthly savings are $%.2f." % savings_monthly)
print("Project savings after one year , with interest, is: $%.2f." % savings_with_interest)
