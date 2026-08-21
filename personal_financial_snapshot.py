def main():
    name = input("Enter your name: ")
    monthly_income = float(input("Enter your monthly income: "))
    monthly_housing_cost = float(input("Enter your monthly housing cost: "))
    monthly_food_cost = float(input("Enter your monthly food cost: "))
    monthly_transportation_cost = float(input("Enter your monthly transportation cost: "))
    other_monthly_expenses = float(input("Enter your other monthly expenses: "))
    savings_goal = float(input("Enter your savings goal: "))


    total_expenses = monthly_housing_cost + monthly_food_cost + monthly_transportation_cost + other_monthly_expenses
    monthly_savings = monthly_income - total_expenses
    annual_savings = monthly_savings * 12
    savings_percentage = (monthly_savings / monthly_income) * 100
    months_to_goal = savings_goal / monthly_savings


    


    print("PERSONAL FINANCIAL SNAPSHOT")
    print(f"Name: {name}")
    print(f"Monthly Income: ${monthly_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Monthly Savings: ${monthly_savings:.2f}")
    print(f"Annual Savings: ${annual_savings:.2f}")
    print(f"Savings rate: {savings_percentage:.2f}%")
    print(f"Months to Goal: {months_to_goal:.2f}")
    


main()



