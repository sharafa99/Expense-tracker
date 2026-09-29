
def id_generator(expenses):
    
    if len(expenses) == 0:
        return 1
    else:
        id_list = map(int, expenses.keys())
        return max(id_list) + 1

def add_expense(new_expense, expenses):
    modified_expenses = {}
    modified_expenses.update(expenses)
    expense_id = id_generator(expenses)
    modified_expenses[expense_id] = new_expense
    return modified_expenses

def calculate_total(expenses):
    total = 0

    for key in expenses:
        total += expenses[key]["Amount"]

    return round(total,2)

def calculate_number_of_expenses(expenses):
    return len(expenses)

def calculate_average(total_expenses, len_expenses):
    if len_expenses == 0:
        return 0
    
    return round(total_expenses/len_expenses,2)

def building_spending_summary(total_spending, len_expenses, average):
    spending_summary = {}
    spending_summary["Total spending"] = total_spending
    spending_summary["Number of expenses"] = len_expenses
    spending_summary["Average expense"] = average
    return spending_summary