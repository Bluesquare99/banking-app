from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class TransactionType(str, Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"


class Transaction(BaseModel):
    user_id: int
    transaction_type: TransactionType
    amount: int


@app.get("/")
async def root():
    return "Welcome to Max's bank!"


@app.post("/transaction/{user_id}")
async def transaction(user_id: int, transaction: Transaction):
    return transaction
