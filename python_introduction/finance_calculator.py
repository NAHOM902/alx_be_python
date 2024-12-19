monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expense: "))

monthly_saving = float(monthly_income) - float(monthly_expenses)
print(f"Your monthly savings are ${monthly_saving:.1f}.")

annual_saving = monthly_saving * 12 + (monthly_saving * 0.05 * 12)
print(f"Projected savings after one year, with interest, is: ${annual_saving:.1f}.")

    # income = float(input("Enter your monthly income: "))
    # expenses = float(input("Enter your total monthly expenses: "))

    # # Step 2: Calculate monthly savings
    # monthly_savings = income - expenses

    # # Step 3: Project annual savings with interest
    # annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

    # # Step 4: Display results
    # print(f"Your monthly savings are ${monthly_savings:.2f}.")
    # print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")