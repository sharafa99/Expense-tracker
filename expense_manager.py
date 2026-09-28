
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
