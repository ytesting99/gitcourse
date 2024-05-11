# Git for developers: managing workflows and conflicts

Codebase for Guided Project "Git for developers: managing workflows and conflicts" on Coursera platform

## Basic project setup

- Install virtual enviroment with its dependencies: `poetry install`
- Activate it: `poetry shell`
- To run the API, use the command: `uvicorn src.app:app --reload`

## Ready-to-use code

- Update items API route
```python
@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    conn = get_db()
    conn.execute(
        "UPDATE items SET name = ?, price = ?, is_offer = ? WHERE id = ?",
        (item.name, item.price, int(item.is_offer) 
        if item.is_offer 
        else None, item_id),)
    conn.commit()
    return item
```
- Delete items API route
```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    conn = get_db()
    conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    return {"message": "Item deleted"}
```
- Read items API route
```python
@app.get("/items/")
def read_items():
    conn = get_db()
    items = conn.execute("SELECT * FROM items").fetchall()
    return [
        dict(item) for item in items]
```
- Read item API route
```python
@app.get("/items/{item_id}")
def read_item(item_id:int):
    conn = get_db()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    if item is None:
        raise HTTPException(
            status_code=404, 
    detail="Item not found"
            )
    return dict(item)
```

## Conventional commit styles

![commit styles](./img/comimt-style.png)