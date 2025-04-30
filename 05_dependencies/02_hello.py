from fastapi import FastAPI, Depends, Query, HTTPException


app : FastAPI = FastAPI()

def dep_check(name:str = Query(None), password:str = Query(None)):
    if not name:
       raise HTTPException(status_code=400, detail="Name is required")

    
@app.get("/login", dependencies=[Depends(dep_check)])
def login():
    return True