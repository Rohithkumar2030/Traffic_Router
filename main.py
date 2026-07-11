import os
import time
import random
from fastapi import FastAPI

app = FastAPI()

POD_NAME = os.getenv("POD_NAME","local-dev")
VERSION = os.getenv("VERSION","v1")


@app.get("/")
async def root():

    if VERSION == "v1":
        performance = "standard"

    elif VERSION == "v2":
        r = random.random()
        performance = "beta-stable"

        if r < 0.05:
            performance = "crashing"
            do_crash()      # 5% crash

        elif r < 0.10:
            performance = "lagging due to high latency"
            do_lag()        # 5% lag

        elif r < 0.20:
            performance = "loading due to high-cpu-load"
            do_load()       # 10% CPU load

    elif VERSION == "v3":
        performance = "optimized-low-latency"

    response = {
        "message": "Smart Traffic Router",
        "version": VERSION,
        "pod_name": POD_NAME,
        "performance": performance
    }
    return response


@app.get("/health")
async def health():
    return {
        "status": "200 OK",
        "version": VERSION,
    }

def do_crash():
    print(f"CRASHING POD: {POD_NAME}, VERSION: {VERSION}",flush=True)
    os._exit(1)

@app.get("/simulate/crash")
async def crash():
    do_crash()

def do_load():
    total = 0
    for i in range(10**8):
        total += i
    return total

@app.get("/simulate/load")
async def load():
    do_load()
    return {
        "message": "Loading took some time but its fine now"
    }

def do_lag():
    time.sleep(10)

@app.get("/simulate/lag")
async def lag():
    do_lag()
    return {
        "message": "Delayed response",
        "delay": "10s"
    }

