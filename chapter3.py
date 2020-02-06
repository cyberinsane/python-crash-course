"""
Chapter 3
- Fast API
- GET expenses
- POST expense
- Create Schema(s)

Install uvicorn server
$ pip3 install uvicorn

Install FastApi
$ pip3 install fastapi


Deploy server on local host
expense:app --port 8000

Deploy on Lan
expense:app --host 0.0.0.0 --port 8000

"""

import uuid
from fastapi import FastAPI
from schema import ExpenseSchema, ExpenseBody

app = FastAPI()

# List to track save expenses
expenses: [ExpenseSchema] = []


@app.get('/expenses')
def get_expenses():
    return expenses


@app.post('/expense')
def add_expense(item: ExpenseBody):
    value = ExpenseSchema(**item.dict(), id=str(uuid.uuid4()))
    expenses.append(value)
    return value
