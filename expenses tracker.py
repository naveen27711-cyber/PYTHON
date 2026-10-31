import json

expenses = []

def load_expenses():
    try:
        with open("Expenses tracker","r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    

def add_expenses():
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError :
            print("Amount must in numbers!")


    category = input("Enter category: ")
    date = input("Enter date: ")
    note = input("Enter note: ")

    new_expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "note": note
    }
    expenses.append(new_expense)

    with open("Expenses tracker", "w") as f:
        json.dump(expenses, f)

    return "Expense added successfully!"

def view_expenses():
    if not expenses:
        return "expenses is empty!"
    print("==== Your Expenses ====")

    for e in expenses:
        print(e)
expenses = load_expenses()



def monthly_expenses():
    month = input("enter year and month : ")
    found = False
    print("==== Your Monthly Expenses ====")
    for e in expenses:
        if  e["date"][:7] == month[:7]:
            print(e)
            found = True  
    if not found:
        print("No expenses found!")            
 


while True:
    print("\n==== Expenses Tracker ====")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Monthly expenses")
    print("4. Exit")
 
    user_choice = input("Enter choice: ")
 
    if user_choice == "1":
        print(add_expenses())

    elif user_choice == "2":
        view_expenses()

    elif user_choice == "3":
        monthly_expenses()

    elif user_choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")