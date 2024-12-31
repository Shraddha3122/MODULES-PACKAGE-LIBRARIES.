# finance/budget.py

def create_budget(income, expenses):
    """
    Create a simple budget summary.

    :param income: Total income
    :param expenses: List of expenses
    :return: A dictionary with total income, total expenses, and remaining balance
    """
    total_expenses = sum(expenses)
    remaining_balance = income - total_expenses
    budget_summary = {
        'Total Income': income,
        'Total Expenses': total_expenses,
        'Remaining Balance': remaining_balance
    }
    return budget_summary