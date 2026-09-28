
def expense(amount, category, description, expense_date):
    expense_data = {}
    expense_data["Amount"] = amount
    expense_data["Category"] = category
    expense_data["Description"] = description
    expense_data["Date"] = expense_date
    return expense_data
