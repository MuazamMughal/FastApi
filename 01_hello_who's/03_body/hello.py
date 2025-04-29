from fastapi import FastAPI, Body
app: FastAPI = FastAPI()

app.post("/hello")
def hello(name: str = Body(embed=True)):
    return {"message": f"Hello {name}"}

