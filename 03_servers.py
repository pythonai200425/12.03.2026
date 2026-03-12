from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# pip install uvicorn
# pip install fastapi
# uvicorn 03_servers:app --port 8000 --reload
# swagger = http://127.0.0.1:8000/items
# swagger = http://127.0.0.1:8000/docs

# if page not reloaded change the port


app = FastAPI()

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

# ---- PUT update full ----
# dict1['danny'] = 90
# update , if not exist create (replace null)

# ---- PATCH partial update ----
# update only, if not exist -- error

# ---- DELETE ----
@app.delete("/items/{item_id}")
def delete_item_by_id(item_id: int):
    return {"message": f"item {item_id} deleted"}
