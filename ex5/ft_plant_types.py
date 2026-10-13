#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, _height: float, _age: int) -> None:
        self.name = name.capitalize()
        self._height = round(_height, 1)
        self._age = _age

    def show(self) -> None:
        print(f"{self.name}: {self._height} cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, _height: float, _age: int,
                 color: str) -> None:
        super().__init__(name, _height, _age)
        self.color = color
        self.bloom_status = False

    def show(self) -> None:
        print(f"{self.name}: {self._height} cm, {self._age} days old\n"
              f" Color: {self.color}")
        if self.bloom_status is False:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self.bloom_status = True
        if self.bloom_status is True:
            self.show()
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, _height: float, _age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, _height, _age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        print(f"{self.name}: {self._height} cm, {self._age} days old\n"
              f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"{self.name} now produces a shade of {self._height}cm long and "
              f"{self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, _height: float, _age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, _height, _age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(f"{self.name}: {self._height} cm, {self._age} days old\n"
              f" Harvest_season: {self.harvest_season}\n"
              f" Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        self._height += 42
        self._age += 20

    def grow(self, grow_day: int) -> None:
        print(f"[make {self.name} grow and age for {grow_day} days]")
        self.age()
        self.nutritional_value += grow_day
        self.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower('Rose', 15.0, 10, 'Red')
    rose.show()
    rose.bloom()
    print()
    print("=== Tree")
    oak = Tree('Oak', 200.0, 365, 5)
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable('Tomato', 5.0, 10, 'April', 0)
    tomato.show()
    tomato.grow(20)
