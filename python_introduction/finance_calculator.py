monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expense: "))

monthly_saving = monthly_income - monthly_expense
print(f"Your monthly savings are ${monthly_saving}.")

annual_saving = monthly_saving * 12 + (monthly_saving * 0.05 * 12)
print(f"Projected savings after one year, with interest, is: ${int(annual_saving)}.")
