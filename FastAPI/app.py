from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import uvicorn
import os
from fastapi.responses import FileResponse

class Tea(BaseModel):
    id : int 
    name: str
    origin: str
    
app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

teas: List[Tea] = []

@app.get("/")
def read_root():
    template_path = os.path.join(os.path.dirname(__file__), "templates")
    return FileResponse(os.path.join(template_path, "index.html"), media_type="text/html")

@app.get("/getteas/")
def get_teas():
    return teas

@app.post("/addteas/")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/updatetea/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/deletetea/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            delete_tea = teas.pop(index)
            return delete_tea
        return {"message": "Tea not found"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

