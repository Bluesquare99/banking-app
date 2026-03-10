from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

volume_path = Path("/ledger")
stocks_file = Path("stock.txt")
ledger = volume_path / stocks_file if volume_path.exists() else stocks_file 
with open(ledger, 'w') as f:
    f.write('0')

class OrderType(str, Enum):
    buy = "buy"
    sell = "sell"

class Order(BaseModel):
    order_type: OrderType
    amount: int

def enter_order(order: Order):
    with open(ledger, 'r') as f:
        cur_price = int(f.read())
    if order.order_type == OrderType.buy:
        cur_price += order.amount
    elif order.order_type == OrderType.sell:
        cur_price -= order.amount
    with open(ledger, 'w') as f:
        f.write(str(cur_price))


@app.get("/")
async def root():
    return "Welcome to Max's exchange!"


@app.post("/order/")
async def order(order: Order):
    enter_order(order)
    return order
