from fastapi import FastAPI
app : FastAPI = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "so this is after i run server as auto reload"}



#so i wrote the first ever fast api
