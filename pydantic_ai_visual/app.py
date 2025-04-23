import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query

CURRENT_SERVER_LOCATION = os.environ.get("CURRENT_SERVER_LOCATION", "http://localhost:8891")


@asynccontextmanager
async def lifespan(app: FastAPI):
    openapi_schema = app.openapi()
    openapi_schema["servers"] = [
        {"url": CURRENT_SERVER_LOCATION, "description": "Current Server"},
    ]
    app.openapi_schema = openapi_schema
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.post("/visualize")
async def visualize_post():
    return {"message": "Hello World"}


@app.get("/visualize")
async def visualize_get(url: str = Query(..., description="The url to visualize")):
    return {"message": "Hello World"}
