import json
import os.path


file_path = "expenses.json"

expenses = {}
monthly_total = 0.0
one_off_total = 0.0

##  Get users input by asking questions    ##
def get_user_input():
    print("\n")
    print("1: Add Expense.")
    print("2. View Expenses.")
    print("3. Calculate Expenses.")
    print("4. Save Expenses.")
    print("5. Exit Program.")
    choice = input("Choice: ")
    return choice

##  Add expenses to the expenses variable (staging for expenses.json)   ##
def add_expense():
    name = input("Enter Name of Expense service: ")
    date = input("Enter Date of Expense (MM-DD-YYYY): ")
    while True:
        try:
            category = chr(input("Enter One off or Recurring expense (o,r): "))
            break
        except ValueError:
            print("Invalid input. Needs to be a chr.")
    while True:
        try:
            amount = float(input("Enter Expense Amount 0.00: "))
            break
        except ValueError:
            print("Invalid input. Neews to be a float or int.")
    description = input("Description of Expense: ")
    
    expense = {
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses[name] = expense

##  View current expenses by name of expense    ##
def view_expenses():
    if not expenses:
        print("\nNo current expenses.")
    else:
        for expense_name, details in expenses.items():
            print(f"\nExpense: {expense_name}")
            for key, value in details.items():
                print(f"{key}: {value}")

##  Calculate all Recurring and One off expenses    ##
def calculate_expenses():
    if not expenses:
        print("\nNo current expenses.")
    else:
        global monthly_total 
        global one_off_total
        monthly_total = 0.0
        one_off_total = 0.0
        for expense, details in expenses.items():
            for key, value in details.items():
                if key == 'category' and value.startswith(('R','r')):
                    monthly_total += float(details['amount'])
                    one_off_total += float(details('amount'))
                elif key == 'category' and value.startswith(('O','o')):
                    one_off_total += float(details['amount'])
        print(f"\n Your recurring monthly total is: {monthly_total}")
        print(f"\n Your charges this month are: {one_off_total}")


##  Save all expenses in expenses variable to expenses.json   ##
def save_expenses():
    if not expenses:
        print("\nNo current expenses.")

    else:
        with open(file_path, "w") as json_file:
            json.dump(expenses, json_file) 
            print("\nSaved to expenses.json")
            json_file.close()

##  Load expenses from file if it exists    ##
def load_expenses():
    if not os.path.isfile(file_path):
        print("No current expense save.")
    else:
        #for expense in enumerate(expenses, start=1):
        global expenses
        with open(file_path, "r") as f:
            expenses = json.load(f)
            print("Expenses loaded.") 
            f.close()

##  Core functions / loop to load program and gather inputs    ##
print("Attempting to load save file...")
load_expenses()

while True:
    choice = get_user_input()
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        calculate_expenses()
    elif choice == '4':
        save_expenses()
    elif choice == '5':
        print("Closing down expense tracker.")
        break
    else:
        print("Invalid input.")