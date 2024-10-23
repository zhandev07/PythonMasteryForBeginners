import os
import json
from collections import defaultdict
from datetime import datetime

# Function to validate the date
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to save expenses to a file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Function to load expenses from a file
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    return []

# Function to add an expense
def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category (e.g., food, transport): ").strip()
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        if not validate_date(date):
            raise ValueError("Invalid date format! Use YYYY-MM-DD.")
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)
        print(f"Added: {amount} in {category} on {date}.")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded!")
    else:
        print(f"{'No':<5}{'Date':<12}{'Category':<15}{'Amount':<10}")
        print("=" * 40)
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx:<5}{expense['date']:<12}{expense['category']:<15}{expense['amount']:<10}")

# Function to delete an expense
def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete!")
    else:
        view_expenses(expenses)
        try:
            index = int(input("Enter the index of the expense to delete: "))
            if 0 <= index < len(expenses):
                deleted = expenses.pop(index)
                save_expenses(expenses)
                print(f"Deleted expense: {deleted['amount']} in {deleted['category']}.")
            else:
                print("Invalid index!")
        except ValueError:
            print("Please enter a valid index.")

# Function to show monthly summary of expenses
def monthly_summary(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        month = expense["date"][:7]  # Extract YYYY-MM from the date
        summary[month] += expense["amount"]
    print(f"{'Month':<10}{'Total':<10}")
    print("=" * 20)
    for month, total in summary.items():
        print(f"{month:<10}{total:<10}")

# Function to show category breakdown of expenses
def category_breakdown(expenses):
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]
    print(f"{'Category':<15}{'Total':<10}")
    print("=" * 25)
    for category, total in summary.items():
        print(f"{category:<15}{total:<10}")

# Main menu to interact with the app
def main_menu():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Delete an Expense")
        print("4. View Monthly Summary")
        print("5. View Category Breakdown")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            monthly_summary(expenses)
        elif choice == "5":
            category_breakdown(expenses)
        elif choice == "6":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
