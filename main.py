import random
from fastapi import FastAPI, Request
import requests
from pydantic import BaseModel

app = FastAPI()
url = "https://api.ultramsg.com/instance14131/messages/chat"

@app.get("/healthz")
async def root():
    return "ok"

@app.post("/blog")
async def get_body(request: Request):
    data=await request.json()
    print(data)
    if data["data"]["to"]=='917720063009@c.us' and data["data"]["body"]=="otp":
            opt=random.randint(1000,9999)
            payload = f"token=j6zub8czi2qjp57p&to=+917720063009,&body={opt}&priority=10&referenceId="
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requests.request("POST", url, data=payload, headers=headers)
    return ""

