"""
Chapter 1
- Basic python file creation
- Functions
- Args
- Print

"""


def get_expenses():
    return {"message": "No expenses"}


def add_expense(amount: float, description: str, month: str):
    # print(f"you added {amount} for {description} on {month}")
    return {"message": f"you added {amount} for {description} on {month}"}


# Test
add_expense(400, "Light Bill", "April")