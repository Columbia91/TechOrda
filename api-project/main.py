from fastapi import FastAPI, HTTPException, Header, Body
from typing import Optional
import json

# Создаем объект приложения FastAPI
app = FastAPI()

# Определяем маршрут на корневой запрос "/"
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Глобальный массив для сохранения элементов
global_list = []

@app.get("/sum1n/{n}")
def sum1n(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="n must be a positive integer")
    result = sum(range(1, n + 1))
    return {"result": result}


@app.get("/fibo")
def fibo(n: int):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return fibo(n - 1) + fibo(n - 2)


@app.post("/reverse")
def reverse_string(string: Optional[str] = Header(None)):
    if not string:
        raise HTTPException(status_code=400, detail="Header 'string' is required")
    return {"result": string[::-1]}


@app.put("/list")
def add_to_list(element: dict = Body(...)):
    if "element" not in element:
        raise HTTPException(status_code=400, detail="Key 'element' is required")
    global_list.append(element["element"])
    return {"result": global_list}


@app.get("/list")
def get_list():
    return {"result": global_list}


@app.post("/calculator")
def calculator(expr: dict = Body(...)):
    if "expr" not in expr:
        raise HTTPException(status_code=400, detail="Key 'expr' is required")
    try:
        num1, operator, num2 = expr["expr"].split(",")
        num1, num2 = float(num1), float(num2)
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid")
    if operator == "+":
        return {"result": num1 + num2}
    elif operator == "-":
        return {"result": num1 - num2}
    elif operator == "*":
        return {"result": num1 * num2}
    elif operator == "/":
        if num2 == 0:
            raise HTTPException(status_code=403, detail="zerodiv")
        return {"result": num1 / num2}
    else:
        raise HTTPException(status_code=400, detail="invalid")