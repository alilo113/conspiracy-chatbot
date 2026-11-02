from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a Pydantic model for the input payload
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

@app.post('/items/')
async def create_item(item: Item):
    # Validate the input payload
    if item.price < 0 or item.quantity < 0:
        raise HTTPException(status_code=400, detail='Price and quantity must be non-negative.')

    # Process the item (e.g., save to database)
    # For demonstration, we'll just return a confirmation response

    return Response(content='Item created successfully', status_code=201)

app = FastAPI()

@app.post('/api/data')
def process_data(data: dict):
    return {'status': 'success', 'data': data}
