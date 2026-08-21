monthly_salary = float(input("Enter your monthly salary: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_salary - monthly_expenses
annual_savings = monthly_savings * 12
print(f"Your monthly savings are: {monthly_savings}")
print(f"Your annual savings are: {annual_savings}")

