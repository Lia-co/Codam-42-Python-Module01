#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0
            self._shade_count: int = 0
            self._shade_status: bool = False

        def grow_increment(self) -> None:
            self._grow_count += 1

        def age_increment(self) -> None:
            self._age_count += 1

        def show_increment(self) -> None:
            self._show_count += 1

        def shade_increment(self) -> None:
            if self._shade_status is True:
                self._shade_count += 1

        def show(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count} age,"
                  f" {self._show_count} show")
            if self._shade_status is True:
                print(f" {self._shade_count} shade")

    def __init__(self, name: str, _height: float, _age: int) -> None:
        self.name = name.capitalize()
        self._height = round(_height, 1)
        self._age = _age
        self._stats = Plant.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height} cm, {self._age} days old")
        self._stats.show_increment()

    @staticmethod
    def check_age(age: int) -> None:
        if age >= 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> Flase")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, _height: float, _age: int,
                 color: str) -> None:
        super().__init__(name, _height, _age)
        self.color = color
        self.bloom_status = False

    def show(self) -> None:
        self._stats.show_increment()
        print(f"{self.name}: {self._height} cm, {self._age} days old\n"
              f" Color: {self.color}")
        if self.bloom_status is False:
            print(f"{self.name} has not bloomed yet")

    def grow(self, len_grow: float) -> None:
        self._height += len_grow
        self._stats.grow_increment()

    def age(self) -> None:
        self._stats.age_increment()

    def bloom(self) -> None:
        self.bloom_status = True
        if self.bloom_status is True:
            self.show()
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, _height: float, _age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, _height, _age)
        self.trunk_diameter = trunk_diameter
        self._stats._shade_status = True

    def show(self) -> None:
        self._stats.show_increment()
        print(f"{self.name}: {self._height} cm, {self._age} days old\n"
              f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.shade_increment()
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


class Seed(Flower):
    def __init__(self, name: str, _height: float, _age: int,
                 color: str, seed: int) -> None:
        super().__init__(name, _height, _age, color)
        self.bloom_status = False
        self.seed = seed

    def show(self) -> None:
        self._stats.show_increment()
        print(f"{self.name}: {self._height} cm, {self._age} days old\n"
              f" Color: {self.color}\n"
              f" Seeds: {self.seed}")
        if self.bloom_status is False:
            print(f"{self.name} has not bloomed yet")

    def age(self) -> None:
        self._stats.grow_increment()
        self._height += 30
        self._age += 20

    def grow(self, grow_day: float) -> None:
        self._stats.age_increment()
        self.seed += 42


def show_stats(plant: Plant) -> None:
    plant._stats.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print()

    print("=== Flower")
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    # hardcode, other way?
    print("[statistics for Rose]")
    show_stats(rose)
    print("[asking the Rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    print("[statistics for Rose]")
    show_stats(rose)
    print()

    print("=== Tree")
    oak = Tree('Oak', 200.0, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed('sunflower', 80.0, 45, 'yellow', 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age()
    sunflower.bloom()
    print("[statistics for Sunflower]")
    show_stats(sunflower)
    print()

    print("=== Anonymous")
    unknown_plant = Plant.anonymous()
    unknown_plant.show()
    print("[statistics for Unknown plant]")
    show_stats(unknown_plant)
