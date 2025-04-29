from fastapi import FastAPI
app :FastAPI = FastAPI()

@app.get("/hello/{name}")

def urlpath(name: str):
    return {"message": f"Hello {name}!"}

# now amnking another rout in the same file

@app.get("/hello/{name}/age/{age}")
def helloname_age(name:str , age:int):
    return {"message": f"Hello {name}!, your age is {age}"}