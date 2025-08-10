from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import webbrowser
import threading


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
    
@app.middleware("http")
async def capture_host_port(request: Request, call_next):
    """
    Capture host and port dynamically from incoming requests.
    """
    if not hasattr(app.state, "host_url"):
        app.state.host_url = str(request.base_url)
    response = await call_next(request)
    return response

@app.on_event("startup")
def startup_event():
    def open_browser():
        # Wait until host_url is captured from first request
        while not hasattr(app.state, "host_url"):
            pass
        webbrowser.open_new(app.state.host_url + "docs")
    threading.Thread(target=open_browser, daemon=True).start()