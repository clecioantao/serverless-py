from fastapi import FastAPI
from src.env import config

MODE=config("MODE", default="testing")

app = FastAPI()

@app.get("/")
def home_page():
    return {"hello": "world", "mode": MODE}

# @app.post("/")
# def home_handle_data_page():
#     return {"hello": "world"}