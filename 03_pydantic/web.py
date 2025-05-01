from fastapi import FastAPI
from data import Creature
app : FastAPI = FastAPI()

@app.get("/")
def get_all( ) ->list[Creature]:
    from data import get_creatures
    return get_creatures()