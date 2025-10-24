# Expense Tracker
import csv

file = "expenses.csv"

def add_expense():
    name = input("Expense Name: ")
    amount = float(input("Amount (₹): "))
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, amount])
    print("Expense Added!")

def view_expenses():
    print("\n--- All Expenses ---")
    total = 0
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    print(f"{row[0]} - ₹{row[1]}")
                    total += float(row[1])
        print(f"\nTotal: ₹{total}")
    except FileNotFoundError:
        print("No expenses yet!")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        break
    else:
        print("Invalid input!😵")
        print("Suggestion : Please enter a valid option from the menu.")

print("Thank you for using Expense Tracker!")        
