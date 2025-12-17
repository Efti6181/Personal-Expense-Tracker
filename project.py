import json
import csv
from datetime import datetime

JSON_FILE = "expenses.json"
CSV_FILE = "expenses.csv"


def main():
    print("Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View Total Expenses")
    print("3. Generate Report")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input("Expense name: ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        add_expense(name, category, amount)
        print("Expense added successfully.")

    elif choice == "2":
        total = calculate_total()
        print(f"Total Expense: {total} BDT")

    elif choice == "3":
        generate_report()
        print("Report generated.")

    else:
        print("Invalid choice.")


def add_expense(name, category, amount):
    expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses = load_expenses()
    expenses.append(expense)

    with open(JSON_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense["date"], name, category, amount])

    return expense


def load_expenses():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def calculate_total():
    expenses = load_expenses()
    return sum(expense["amount"] for expense in expenses)


def generate_report():
    expenses = load_expenses()
    report = {}

    for expense in expenses:
        category = expense["category"]
        report[category] = report.get(category, 0) + expense["amount"]

    with open("report.txt", "w") as file:
        for category, total in report.items():
            file.write(f"{category}: {total} BDT\n")


if __name__ == "__main__":
    main()
