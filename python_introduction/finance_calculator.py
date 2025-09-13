income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthy expenses: "))

savings_monthly = income - expenses
savings_yearly = savings_monthly * 12

interest_rate = 0.05
savings_with_interest = savings_yearly * (12 + interest_rate)
