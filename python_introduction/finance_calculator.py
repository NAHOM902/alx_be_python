import math
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

projected_savings = math.floor(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest is: ${projected_savings}.")



# monthly_income = int(input("Enter your monthly income: "))
# monthly_expenses = int(input("Enter your total monthly expense: "))

# monthly_saving = monthly_income - monthly_expenses
# print(f"Your monthly savings are ${monthly_saving}.")

# annual_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
# print(f"Projected savings after one year, with interest, is: ${annual_saving}.")

    # income = float(input("Enter your monthly income: "))
    # expenses = float(input("Enter your total monthly expenses: "))

    # # Step 2: Calculate monthly savings
    # monthly_savings = income - expenses

    # # Step 3: Project annual savings with interest
    # annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

    # # Step 4: Display results
    # print(f"Your monthly savings are ${monthly_savings:.2f}.")
    # print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")