#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, st_height: float, st_age: int) -> None:
        self.name = name
        self._height = round(st_height, 1)
        self._age = st_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height} cm, {self._age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height > 0:
            self._height = new_height
            print("Height updated: ", end="")
            print(f"{new_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age > 0:
            self._age = new_age
            print("Age updated: ", end="")
            print(f"{new_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant('Rose', 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print()
    print("Current state: ", end="")
    rose.show()
