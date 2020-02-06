"""
Chapter 4
- Add TinyDB
- Use UUID for creating primary key

Install TinyDB
$ pip3 install tinydb

"""

import re
import uuid
from fastapi import FastAPI
from tinydb import TinyDB, Query
from schema import ExpenseSchema, ExpenseBody

# Initialize fast API
app = FastAPI()

# Initialize tinyDb
db = TinyDB('db.json')
Expense = Query()


@app.get('/expenses')
def get_expenses(month: str = None):
    if month is None:
        return db.all()

    return db.search(Expense.month.matches(month, flags=re.IGNORECASE))


@app.post('/expense')
def add_expense(item: ExpenseBody):
    value = ExpenseSchema(**item.dict(), id=str(uuid.uuid4()))
    db.insert(value.dict())
    return value
