"""
Chapter 6
- Serve custom HTTP response
- Jinja2 html templates

Install Jinja2
$ pip3 install jinja2

"""


import uuid
import re
from fastapi import FastAPI, HTTPException
from tinydb import TinyDB, Query
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from schema import ExpenseSchema, ExpenseBody

# Initialize fast API
app = FastAPI()

# Initialize tinyDb
db = TinyDB('db.json')
Expense = Query()

# Get Jinja2 templates
templates = Jinja2Templates(directory="templates")


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


@app.get('/details')
def get_details_html(request: Request, month: str = None):
    header = 'All Expenses' if month is None else f"Expenses for {month}"
    response = templates.TemplateResponse("expense.html",
                                          {"request": request, "title": "Expenses", "body": get_expenses(month),
                                           "header": header})
    return HTMLResponse(content=response.body, status_code=200)


def is_valid_month(month: str):
    return month.lower() in (item.lower() for item in months)
