#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def grow(self, len_grow: float) -> None:
        self.height += len_grow

    def age(self) -> None:
        self.day += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.day} days old")


if __name__ == "__main__":
    rose = Plant('Rose', 25, 30)
    sunflower = Plant('Sunflower', 80, 45)
    cactus = Plant('Cactus', 15, 120)
    week = range(1, 8)
    original_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for n in week:
        print(f"===Days {n}===")
        rose.grow(0.8)
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - original_height, 1)}cm")
