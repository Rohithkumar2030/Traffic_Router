import os
import time
from fastapi import FastAPI

app = FastAPI()

POD_NAME = os.getenv("POD_NAME","local-dev")
VERSION = os.getenv("VERSION","v1")

@app.get("/")
async def root():
    response = {
        "message": "Smart Traffic Router",
        "version": VERSION,
        "pod_name": POD_NAME,
        "performance": "standard"
    }
    
    if VERSION == "v3":
        response["performance"] = "optimized-low-latency"
        
    return response

@app.get("/health")
async def health():
    return {
        "status": "200 OK",
        "version": VERSION,
    }

@app.get("/simulate/crash")
async def crash():
    os._exit(1)
    return {
        "pod_name": POD_NAME,
        "version": VERSION
    }

@app.get("/simulate/load")
async def load():
    count = 0
    for i in range(10**8):
        count += i
    return {
        "message": "Loading took some time but its fine now"
    }

@app.get("/simulate/lag")
async def lag():
    time.sleep(10)
    return {
        "message": "Delayed response",
        "delay": "10s"
    }