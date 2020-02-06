from pydantic import BaseModel


# Expense Body
class ExpenseBody(BaseModel):
    amount: float
    description: str
    month: str


# Expense Schema
class ExpenseSchema(ExpenseBody):
    id: str
