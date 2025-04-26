from fastapi import FastAPI

app : FastAPI= FastAPI()

@app.get("/hello/")
def getingquery(filter:str):
    return {"message": f"Hello {filter}"}