principle = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a percentage): "))
time = int(input("Enter the time period (in years): "))
interest = (principle * rate * time) / 100
print(f"The simple interest is: {interest}")

