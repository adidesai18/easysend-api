import random
from fastapi import FastAPI, Request
import requests
import uvicorn

# create instance of FastAPI
app = FastAPI()
url = "https://api.ultramsg.com/instance14131/messages/chat"



@app.post('/blog')
async def get_body(request: Request):
    data=await request.json()
    print(data)
    if data["data"]["to"]=='917720063009@c.us' and data["data"]["body"]=="opt":
            opt=random.randint(1000,9999)
            payload = f"token=j6zub8czi2qjp57p&to=+917720063009,&body={opt}&priority=10&referenceId="
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requests.request("POST", url, data=payload, headers=headers)
    # await print(request.json())
    return ""



# if __name__=="__main__":
#     # uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
#     uvicorn.run(app=app,host="127.0.0.1",port=8000,reload=True)