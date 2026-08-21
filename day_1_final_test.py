name = input("Enter your name: ")
age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
annual_savings = (monthly_income - monthly_expenses) * 12
savings_rate = ((monthly_income - monthly_expenses) / monthly_income) * 100
goal_amount = float(input("Enter your savings goal: "))
reach_goal = goal_amount / (monthly_income - monthly_expenses)

print  (f"Hello, {name}")
print(f"You are {age} years old.")
print(f"Annual Savings: ${annual_savings:.2f}")
print(f"Savings Rate: {savings_rate:.2f}%")
print(f"if you maintain this savings rate you will save ${goal_amount:.2f} in {reach_goal:.2f} months")
