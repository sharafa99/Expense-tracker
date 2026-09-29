# Imports
import os
import storage
import expense_manager
import models
import time
import datetime

#Header design
def header(head):
    print("="*40)
    print(f"             {head}               ")
    print("="*40)

# Clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_expense(new_expense):
    print("\n")
    print("="*87)
    print(f"| DATE{'':>10} | AMOUNT{'':>5} | CATEGORY{'':>15} | DESCRIPION{'':>16} |")
    print("|","="*83,"|", end="")
    print("")

    print(f"| {new_expense["Date"]:<15}| {new_expense["Amount"]:<11} | {new_expense["Category"]:<23} | {new_expense["Description"]:<26} |")
    print("="*87)
    
    print("\n")

def date_generator():
    print("1. Use today's date\n2. Enter date manually")
    while True:
        try:
            date_option = int(input("Select 1 or 2 for a date option: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if date_option not in (1, 2):
            print("Please choose 1 or 2")
            continue
        break

    if date_option == 1:
        today_date = datetime.date.today()
        expense_date = today_date.strftime("%Y-%m-%d")
        
    else:
        while True:
            date_text = input("Input your date here in the format (YYYY-MM-DD): ")
            try:
                converted_date = datetime.datetime.strptime(date_text, "%Y-%m-%d")
            except ValueError:
                print("Error: Please input a value date")
                continue
            break

        expense_date = converted_date.date()
        expense_date = expense_date.strftime("%Y-%m-%d")

    return expense_date

def view_expense(expenses):
    if len(expenses) == 0:
        print("No expense found!")

    else:
        print("="*102)
        print(f"| ID{'':>5} | DATE{'':>10} | AMOUNT{'':>10} | CATEGORY{'':>15} | DESCRIPION{'':>16} |")
        print("|","="*98,"|", end="")
        print("")

        for key in expenses:

            print(f"| {key:<7} | {expenses[key]["Date"]:<15}| {expenses[key]["Amount"]:<16} | {expenses[key]["Category"]:<23} | {expenses[key]["Description"]:<26} |")
        print("="*102)


# Collection of expenses
expenses = storage.load_storage("expenses.json")

while True:
    clear_terminal()
    header("Expense Tracker")
    print("\n")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View spending summary")
    print("4. View category summary")
    print("5. Delete expense")
    print("6. Exit")
    print("\n")

    while True:
        try:
            choice = int(input('choose an option: ').strip())

        except ValueError:
            print("Please enter a number.")
            continue

        if choice not in (1, 2, 3, 4, 5, 6):
            print("Please choose 1, 2, 3, 4, 5 or 6.")
            continue
        break

    if choice == 1:

        clear_terminal()
        header("Add Expense")
        print("\n")

        # Expense input
        while True:
            try:
                amount = float(input("Insert your expense amount here: "))

            except ValueError:
                print("Invalid input! text or empty text are not allowed. \nPlease insert Numerical values")
                continue

            break

        while True:
            try:
                category = input("What category does the expense falls in: ")

                if not category.strip() or any(char.isdigit() for char in category):
                    raise ValueError("Invalid input! Numbers or empty text are not allowed.")

            except ValueError as e:
                print(f"Error: {e}")
                continue
            break

        while True:
            try:
                description = input("Short expense description: ")

                if not description.strip() or any(char.isdigit() for char in description):
                    raise ValueError("Invalid input! Numbers or empty text are not allowed.")

            except ValueError as e:
                print(f"Error: {e}")
                continue
            break

        expense_date = date_generator()

        new_expense = models.expense(amount, category, description, expense_date)

        display_expense(new_expense)

        latest_expenses = expense_manager.add_expense(new_expense, expenses)

        while True:
            try:
                save_expense = input("Would you like to save the above expense (yes / no): ")
    
                if not save_expense.strip() or any(char.isdigit() for char in save_expense):
                    raise ValueError("Invalid input! Numbers or empty text are not allowed.")
                allowed_words = ["yes","no"]
                if save_expense.lower() not in allowed_words:
                    raise ValueError(f"Please choose from: {', '.join(allowed_words)}")
    
            except ValueError as e:
                print(f"Error: {e}")
                continue
    
            break

        if save_expense == "yes":
            expenses = latest_expenses
            storage.save_expense(expenses, "expenses.json")
            print("\n")
            print(f"Success! Your expense is saved successfully")
            time.sleep(2)
        else:
            print("\n")
            print("Your expense is not saved")
            time.sleep(2)

    if choice == 2:
        clear_terminal()
        header("View Expenses")
        print("\n")
        view_expense(expenses)
        print("\n")
        while True:
            try:
                back = input('Type "back" to return to the main menu: ').strip().lower()
    
                if back != "back":
                    raise ValueError(f'Please type "back" when you are done viewing the expenses: ')
    
            except ValueError as e:
                print(f"Error: {e}")
                continue
    
            break
        
    if choice == 3:
        clear_terminal()
        header("Spending Summary")
        print("\n")

        total_amount = expense_manager.calculate_total(expenses)
        number_of_expenses = expense_manager.calculate_number_of_expenses(expenses)
        average_expense = expense_manager.calculate_average(total_amount, number_of_expenses)
        spending_summary = expense_manager.building_spending_summary(total_amount, number_of_expenses, average_expense)

        print(f"Total expenses:{'':>10} ${spending_summary["Total spending"]}")
        print(f"Number of expenses:{'':>6} {spending_summary["Number of expenses"]}")
        print(f"Average expense:{'':>9} {spending_summary["Average expense"]}")
        print("\n")

        while True:
            try:
                back = input('Type "back" to return to the main menu: ').strip().lower()
    
                if back != "back":
                    raise ValueError(f'Please type "back" when you are done viewing the expenses: ')
    
            except ValueError as e:
                print(f"Error: {e}")
                continue
    
            break
        

    if choice == 4:
        print("View category expense")

    if choice == 5:
        clear_terminal()
        header("Delete Expense")
        print("\n")
        view_expense(expenses)
        print("\n")
        delete_text = input("Delete the expense with the ID number: ")
        delete_expense = expenses.pop(delete_text)
        
        print(f"The deleted expense is :")
        display_expense(delete_expense)
        while True:
            try:
                final_delete = input(f"Are you sure you want to permanently delete the expense with the ID number {delete_text}? (y/n)")
    
                if not final_delete.strip() or any(char.isdigit() for char in final_delete):
                    raise ValueError("Invalid input! Numbers or empty text are not allowed.")
                allowed_words = ["y","n"]
                if final_delete.lower() not in allowed_words:
                    raise ValueError(f"Please choose from: {', '.join(allowed_words)}")
    
            except ValueError as e:
                print(f"Error: {e}")
                continue
    
            break
        if final_delete == "y":
            storage.save_expense(expenses, "expenses.json")
            print("\n")
            print(f"Success! Your expense is permanently deleted successfully")
            time.sleep(2)
        else:
            print("The expense is not permanently deleted\nIt would be retrieved after the re-run of the program")
    if choice == 6:
        break