from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal  

app = FastAPI()

class variable(BaseModel):
    a : int
    b : int

@app.post("/add")
def add_numbers(var: variable):
    return {"result": var.a + var.b}


class parameter(BaseModel):
    a : int
    b : int
    op: Literal["add", "subtract", "multiply", "divide"]


@app.post("/calculator")
def calculator(param: parameter):
    if param.op == "add":
        return {"result" :param.a + param.b}
    elif param.op == "subtract":
        return {"result" :param.a - param.b}
    elif param.op == "multiply":
        return {"result" :param.a * param.b}
    elif param.op == "divide":
        if param.b != 0:
            return {"result" :param.a / param.b}
        else:
            return {"result":"Error: Division by zero"}
    else:
        return {"result":"Error: Unknown operation"}