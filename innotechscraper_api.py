#pip install fastapi

from fastapi import FastAPI
from fastapi import HTTPException
import json
import time

app = FastAPI()


@app.get("/tank_metric")
def read_root():
    try:
        with open('./tank_metric.json', 'r') as tank_metric:
            content = json.load(tank_metric)
        
        #data must be up to date until 6 minutes
        if(time.time() - float(content['epoch_time']) < 360):
            return content['tank']
        else:
            raise HTTPException (
                status_code=409,
                detail={ "message": "Data is not up to date" }
            )
    except:
        raise HTTPException (
            status_code=500,
            detail={ "message": "Server Error" }
        )
