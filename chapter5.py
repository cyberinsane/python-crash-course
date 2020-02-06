"""
Chapter 5
- Method to validate months
- Exception handling

"""


import uuid
import re
from fastapi import FastAPI, HTTPException
from tinydb import TinyDB, Query
from schema import ExpenseSchema, ExpenseBody

# Initialize fast API
app = FastAPI()

# Initialize tinyDb
db = TinyDB('db.json')
Expense = Query()

# List of months for validation
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


@app.get('/expenses')
def get_expenses(month: str = None):
    if month is None:
        return db.all()

    if is_valid_month(month):
        return db.search(Expense.month.matches(month, flags=re.IGNORECASE))
    else:
        raise HTTPException(400, detail=f"{month} is not a valid month")


@app.post('/expense')
def add_expense(item: ExpenseBody):
    value = ExpenseSchema(**item.dict(), id=str(uuid.uuid4()))
    db.insert(value.dict())
    return value


def is_valid_month(month: str):
    return month.lower() in (item.lower() for item in months)

