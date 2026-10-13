#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, st_height: float, st_age: int) -> None:
        self.name = name
        self.height = round(st_height, 1)
        self.day = st_age

    def grow(self, len_grow: float) -> None:
        self.height += len_grow

    def age(self) -> None:
        self.day += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day} days old")


# why the float is printed as int?
def plant_init() -> None:
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Oak', 200, 365)
    cactus = Plant('Cactus', 5, 90)
    peony = Plant('Sunflower', 80, 45)
    oak = Plant('Fern', 15, 120)
    plants = [rose, sunflower, cactus, peony, oak]
    for _ in plants:
        print("Created: ", end="")
        _.show()


if __name__ == "__main__":
    print("=== Garden Factory Output ===")
    plant_init()
