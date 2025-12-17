from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Tea(BaseModel):
    id:int
    name:str
    origin:str
    
teas: List[Tea] = []

@app.get("/")
def readRoot():
    return {"message":"Welcome To Tea Management"}

@app.get("/teas")
def getAllTeas():
    return teas

@app.post("/teas")
def addTea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def updateTea(tea_id: int, updatedTea: Tea):
    for index, tea in enumerate(teas):
        if tea.id  == tea_id:
            teas[index] = updatedTea
            return updatedTea
    return {"error":"Tea Not Found"}

@app.delete("/teas/{tea_id}")
def deleteTea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted
    return {"error":"Tea Not Found"}