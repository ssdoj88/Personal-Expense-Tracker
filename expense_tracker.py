import csv
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0
        self.filename = "expenses.csv"
        self.load_expenses()

    def add_expense(self):
        print("\n=== Add New Expense ===")
        while True:
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        category = input("Enter category (e.g., Food, Travel, Entertainment): ")
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid positive number.")

        description = input("Enter description: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return

        print("\n=== Expense List ===")
        print("Date\t\tCategory\tAmount\tDescription")
        print("-" * 60)
        for expense in self.expenses:
            print(f"{expense['date']}\t{expense['category']}\t${expense['amount']:.2f}\t{expense['description']}")

    def set_budget(self):
        while True:
            try:
                self.monthly_budget = float(input("\nEnter monthly budget: $"))
                if self.monthly_budget <= 0:
                    raise ValueError
                print(f"Monthly budget set to ${self.monthly_budget:.2f}")
                break
            except ValueError:
                print("Please enter a valid positive number.")

    def track_budget(self):
        if self.monthly_budget == 0:
            print("\nPlease set a monthly budget first.")
            self.set_budget()

        total_expenses = sum(expense['amount'] for expense in self.expenses)
        remaining = self.monthly_budget - total_expenses

        print("\n=== Budget Status ===")
        print(f"Monthly Budget: ${self.monthly_budget:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining: ${remaining:.2f}")

        if remaining < 0:
            print("WARNING: You have exceeded your budget!")
        else:
            print(f"You have ${remaining:.2f} left for the month.")

    def save_expenses(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(self.expenses)
        print(f"\nExpenses saved to {self.filename}")

    def load_expenses(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    self.expenses = []
                    for row in reader:
                        row['amount'] = float(row['amount'])
                        self.expenses.append(row)
                print(f"Loaded {len(self.expenses)} expenses from {self.filename}")
            except Exception as e:
                print(f"Error loading expenses: {e}")

def display_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")

def main():
    tracker = ExpenseTracker()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.track_budget()
        elif choice == '4':
            tracker.save_expenses()
        elif choice == '5':
            tracker.save_expenses()
            print("\nThank you for using Personal Expense Tracker!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 