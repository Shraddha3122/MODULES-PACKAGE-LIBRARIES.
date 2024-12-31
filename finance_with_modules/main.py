# main.py

from finance import calculate_loan_payment, calculate_tax, create_budget

# Loan Calculation
principal = 10000  # Loan amount
annual_rate = 0.05  # 5% interest
years = 5  # 5 years
monthly_payment = calculate_loan_payment(principal, annual_rate, years)
print(f'Monthly Payment: ${monthly_payment:.2f}')

# Tax Computation
income = 50000  # Annual income
tax_rate = 0.20  # 20% tax rate
tax_owed = calculate_tax(income, tax_rate)
print(f'Tax Owed: ${tax_owed:.2f}')

# Budgeting
income = 3000  # Monthly income
expenses = [500, 200, 300, 150]  # Monthly expenses
budget_summary = create_budget(income, expenses)
print('Budget Summary:', budget_summary)


