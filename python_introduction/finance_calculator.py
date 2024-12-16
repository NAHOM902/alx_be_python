monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expense: "))

monthly_saving = monthly_income - monthly_expense
print(f"Your monthly savings are ${monthly_saving}.")

annual_saving = monthly_saving * 12 + (monthly_saving * 0.05 * 12)
print(f"Projected savings after one year, with interest, is: ${annual_saving:.2f}.")
