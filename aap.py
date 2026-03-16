expenses = []

def add_expense():
    name = input("input your expense name : ")
    amount = float(input("input your amount : "))
    category = input(" input your category : ")

    expense = {
        "name" : name,
        "amount" : amount,
        "category" : category
    }

    expenses.append(expense)
    print("all the expenses is added successfully ")


def view_expenses():
    if not expenses:
        print("...ops, sorry did't have this one")
        return 
    for expense in expenses:
        print(f"{expense['name']} - ${expense['amount']} expense{['category']}")
 
def total_expense():
    total = sum(expenses['amount'] for exp in expenses)
    print(f"\n total expenses are {total} \n")

while True:
    print(f"\n1. add expenses ")
    print(f"\n2. view expenses")
    print(f"\n3. total ")
    print(f"\n4. exite")

    choice = input("choose option : ")

    if choice == "1":
        add_expense()

    if choice == "2":
        view_expenses()

    if choice == "3":
        total_expense()

    if choice == "4":
        break 

    else:
        print(f"\n invalid choice")