from fastapi import FastAPI
app :FastAPI = FastAPI()

@app.get("/hello/{name}")

def urlpath(name: str):
    return {"message": f"Hello {name}!"}

