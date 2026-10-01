#Functions for Add expenses
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

#Functions for view expenses
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

def build_spending_summary(expenses):
    spending_summary = {}
    total_amount = calculate_total(expenses)
    number_of_expenses = calculate_number_of_expenses(expenses)
    average_expense = calculate_average(total_amount, number_of_expenses)

    spending_summary["Total spending"] = total_amount
    spending_summary["Number of expenses"] = number_of_expenses
    spending_summary["Average expense"] = average_expense
    return spending_summary

def calculate_category_totals(expenses):
    category_totals = {}

    for _, value in expenses.items():
        category = value["Category"]
        amount = value["Amount"]

        if category in category_totals.keys():
            category_totals[category] += amount
        else:
            category_totals[f"{category}"] = amount
    return category_totals

def delete_expense(expenses, expense_id):
    modified_expenses = {}
    modified_expenses.update(expenses)

    delete_expense = modified_expenses.pop(expense_id)
    return modified_expenses, delete_expense