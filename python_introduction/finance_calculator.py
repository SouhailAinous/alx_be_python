monthly_income = float(input("Enter your monthly income: "))
monthly_expenses= float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(Projected_Savings) + ".")