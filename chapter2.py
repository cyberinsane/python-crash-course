"""
Chapter 2
- Create Expense model class
- List to persist expenses
- Looping

"""


# Expense body
class Expense:
    amount: float
    description: str
    month: str


# List to track save expenses
expenses: [Expense] = []


def get_expenses():
    return expenses


def add_expense(amount: float, description: str, month: str):
    expense = Expense()
    expense.amount = amount
    expense.description = description
    expense.month = month
    expenses.append(expense)


# Tests
add_expense(50, "expense1 ", "April")
add_expense(55, "expense2", "April")
add_expense(30, "expense3", "May")
add_expense(50, "expense4", "June")
add_expense(90, "expense5", "August")

for temp in get_expenses():
    print(f"you added {temp.amount} for {temp.description}")
