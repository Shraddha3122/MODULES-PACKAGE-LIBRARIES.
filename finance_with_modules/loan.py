# Design a package named finance with modules for loan calculation, 
#tax computation, and budgeting.

# finance/loan.py

def calculate_loan_payment(principal, annual_rate, years):
    """
    Calculate the monthly payment on a loan.

    :param principal: The total amount of the loan
    :param annual_rate: The annual interest rate (as a decimal)
    :param years: The number of years to pay off the loan
    :return: The monthly payment amount
    """
    monthly_rate = annual_rate / 12
    number_of_payments = years * 12
    if annual_rate == 0:  # Handle zero interest rate
        return principal / number_of_payments
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
    return payment
