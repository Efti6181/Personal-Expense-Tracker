import os
from project import add_expense, load_expenses, calculate_total


def setup_function():
    if os.path.exists("expenses.json"):
        os.remove("expenses.json")


def test_add_expense():
    expense = add_expense("Lunch", "Food", 150)
    assert expense["name"] == "Lunch"
    assert expense["amount"] == 150


def test_load_expenses():
    add_expense("Bus", "Transport", 50)
    expenses = load_expenses()
    assert len(expenses) == 1


def test_calculate_total():
    add_expense("Coffee", "Food", 100)
    add_expense("Snacks", "Food", 50)
    assert calculate_total() == 150
