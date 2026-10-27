expenses_tracker = []

def add_income():
    try:
        income = float(input("enter amount : "))
    except ValueError:
        return "income must in number"
        
    source = input("enter source : ")
    date = input("enter date :")

    result = {"income" : income ,"source" : source, "date" : date}

    expenses_tracker.append(result)
    return "Income added successfully!"

def add_expense():
 
    try:
        amount = float(input("enter amount : "))
    except ValueError:
        return "amount must in number "
            
    category = input("enter category :")
    date = input("enter date :")
    description = input("enter description : ")

    result = {"amount" : amount, "category" : category, "date" : date, "description" : description}
 

    expenses_tracker.append(result)
    return "Expense added successfully!"


def view_expenses():
    if not  expenses_tracker:
        print("No Expenses Added!")
        return

    for e in expenses_tracker:
        if "amount" in e:
            print( e)
          


def cheak_balance():
    total_income = 0
    total_expenses = 0

    for r in expenses_tracker:
        if "amount" in r:
            total_expenses += r["amount"]
        else:
            total_income += r["income"]

    print("Total income :" ,total_income)
    print("Total expenses : ",total_expenses)
    print("Current balance :",total_income - total_expenses)

def exit_program():
    print("Bye Bye")


while True:
    print("===== EXPENSIVE TRACKER =====")
    print("Add income    : 1")
    print("Add expenses  : 2")
    print("View expenses : 3")
    print("Cheak balance : 4")
    print("Exit          : 5")
    print("=" * 30)

    try:
        User_Input = int(input("Enter User Choice : "))
    except ValueError:
        print("Choice Must Be Number Only!")
        continue

    if User_Input == 1:
        print(add_income())
        

    elif User_Input == 2:
        print(add_expense())

    elif User_Input == 3:
        view_expenses()

    elif User_Input == 4:
        cheak_balance()

    elif User_Input == 5:
        exit_program()
        break 
    else:
        print("invalid")
