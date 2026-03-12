from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# pip install uvicorn
# pip install fastapi
# uvicorn main:app --reload
# swagger = http://127.0.0.1:8000/items
# swagger = http://127.0.0.1:8000/docs


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

# ---- POST create ----

# ---- PUT update full ----
# dict1['danny'] = 90
# update , if not exist create (replace null)

# ---- PATCH partial update ----
# update only, if not exist -- error

# ---- DELETE ----