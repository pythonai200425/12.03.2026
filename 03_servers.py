from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# pip install uvicorn
# pip install fastapi
# uvicorn 03_servers:app --port 8000 --reload
# swagger = http://127.0.0.1:8000/items
# swagger = http://127.0.0.1:8000/docs

# if page not reloaded change the port


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


auto_increment = 2
items = [
    # dict == json
    {"id": 1, "name": "Laptop", "price": 1200, "description": "Gaming laptop"},
    {"id": 2, "name": "Phone", "price": 800, "description": "Smartphone"},
]

# ---- GET all ----
@app.get("/items")
def get_items():
    return items

# ---- GET by id ----
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item id={item_id} not found")

# ---- POST create ----
@app.post("/items")
def create_item(item: Item):
    global auto_increment
    auto_increment += 1
    new_item = {
        "id": auto_increment,
        "name" : item.name,
        "price": item.price,
        "description": item.description
    }
    items.append(new_item)
    return {"message": "Item created", "item": new_item,
            "url": f"http://127.0.0.1:8003/items/{new_item['id']}"}


# ---- PUT update full ----
# dict1['danny'] = 90
# update , if not exist create (replace null)
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            new_item = {
                "id": item_id,
                "name": updated_item.name,
                "price": updated_item.price,
                "description": updated_item.description
            }
            items[index] = new_item
            return {"message": "Item replaced", "item": new_item}

    raise HTTPException(status_code=404, detail="Item not found")

# ---- PATCH partial update ----
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

# update only, if not exist -- error
@app.patch("/items/{item_id}")
def patch_item(item_id: int, item_update: ItemUpdate):
    for item in items:
        if item["id"] == item_id:
            # Check each field manually
            if item_update.name is not None:
                item["name"] = item_update.name

            if item_update.price is not None:
                item["price"] = item_update.price

            if item_update.description is not None:
                item["description"] = item_update.description

            return {"message": "Item updated", "item": item}

    raise HTTPException(status_code=404, detail="Item not found")

# ---- DELETE ----
@app.delete("/items/{item_id}")
def delete_item_by_id(item_id: int):
    for i, item in enumerate(items):
        if item["id"] == item_id:
            deleted = items.pop(i)
            return {"message": f"item {item_id} deleted", "deleted item": deleted}
    raise HTTPException(status_code=404, detail=f"Item id={item_id} not found")
