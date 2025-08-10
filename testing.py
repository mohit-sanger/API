from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {

    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35},
    4: {"name": "David", "age": 28},
    5: {"name": "Eve", "age": 22},
    6: {"name": "Frank", "age": 40},
    7: {"name": "Grace", "age": 32}, 
}


@app.get("/")
def home():
    return {"message": "Welcome to the User API. Use /docs to explore."}



class User(BaseModel):
    name: str
    age: int    

@app.put("/users-detail-update/{user_id}")
def user_update(user_id: int,user: User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}            

@app.delete("/users-delete/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}