from database import get_db, startup_event
from fastapi import FastAPI
from models import Item
app = FastAPI()
app.add_event_handler("startup", startup_event)
@app.post("/items/")
def create_item(item:Item):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, price, is_offer) VALUES (?, ?, ?)", (item.name, item.price, int(item.is_offer) if item.is_offer else None), )
    conn.commit()
    item.id = cursor.lastrowid
    return item

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    """API route to update an item from database trought the item id.

    Parameters
    ----------
    item_id : int
        Item unique identification
    item : Item
        The item itself following the Item model

    Returns
    -------
    Item
        The item after it has been added to database
    """
    conn = get_db()
    conn.execute(
        "UPDATE items SET name = ?, price = ?, is_offer = ? WHERE id = ?",
        (item.name, item.price, int(item.is_offer) 
        if item.is_offer 
        else None, item_id),)
    conn.commit()
    return item