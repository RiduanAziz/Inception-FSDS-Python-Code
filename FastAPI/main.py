from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class Tea(BaseModel):
    id : int
    name: str
    origin: str
    flavor: str
    price: float

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Tea House!"}

@app.get("/getteas/")
def get_teas():
    return teas

@app.post("/addteas/")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/updateteas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"message": "Tea not found"}

@app.delete("/deleteteas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            delete_tea = teas.pop(index)
            return delete_tea
        return {"message": "Tea not found"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

