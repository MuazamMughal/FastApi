from fastapi import FastAPI, Body
app: FastAPI = FastAPI()

app.post("/hello")
def hello(name: str = Body(embed=True)):
    return f"Hello {name}"

