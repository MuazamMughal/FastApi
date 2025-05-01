from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    type: str
    habitat: str
    diet: str
    size: str
    lifespan: int

thing = Creature(
        name="T-Rex",
        type="Dinosaur",
        habitat="Land",
        diet="Carnivore",
        size="Large",
        lifespan=30
        )
print("the name of a creature is" , thing.name)