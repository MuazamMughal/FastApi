from fastapi import FastAPI
app : FastAPI = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}



#so i wrote the first ever fast api
