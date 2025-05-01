from model import Creature

_creatures : list[Creature] = [
    Creature(
        name="T-Rex",
        type="Dinosaur",
        habitat="Land",
        diet="Carnivore",
        size="Large",
        lifespan=30
    ),
    Creature(
        name="Triceratops",
        type="Dinosaur",
        habitat="Land",
        diet="Herbivore",
        size="Large",
        lifespan=30
    ),
    Creature(
        name="Pterodactyl",
        type="Dinosaur",
        habitat="Air",
        diet="Carnivore",
        size="Medium",
        lifespan=20
    ),
    Creature(
        name="Stegosaurus",
        type="Dinosaur",
        habitat="Land",
        diet="Herbivore",
        size="Large",
        lifespan=30
    )
]

def get_creatures() -> list[Creature]:
    return _creatures