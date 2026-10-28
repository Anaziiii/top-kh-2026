from abc import ABC, abstractmethod

class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = 0
        self.has_pool = False
        self.has_garage = False

    def __str__(self):
        return f"House(Walls: {self.walls}, Roof: {self.roof}, Doors: {self.doors}, Pool: {self.has_pool}, Garage: {self.has_garage})"

class HouseSpecification:
    def __init__(self):
        self.description = ""

    def add_detail(self, detail: str):
        self.description += detail + "\n"

    def __str__(self):
        return f"--- Technical Documentation ---\n{self.description}"

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def set_walls(self, material: str):
        pass
    @abstractmethod
    def set_roof(self, roof_type: str):
        pass
    @abstractmethod
    def set_doors(self, count: int):
        pass
    @abstractmethod
    def set_pool(self, has_pool: bool):
        pass
    @abstractmethod
    def set_garage(self, has_garage: bool):
        pass

class HouseBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    def set_walls(self, material: str):
        self._house.walls = material

    def set_roof(self, roof_type: str):
        self._house.roof = roof_type

    def set_doors(self, count: int):
        self._house.doors = count

    def set_pool(self, has_pool: bool):
        self._house.has_pool = has_pool

    def set_garage(self, has_garage: bool):
        self._house.has_garage = has_garage

    def get_result(self) -> House:
        product = self._house
        self.reset()
        return product

class HouseSpecificationBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._specification = HouseSpecification()

    def set_walls(self, material: str):
        self._specification.add_detail(f"Walls built with material: {material}.")

    def set_roof(self, roof_type: str):
        self._specification.add_detail(f"Roof installed of type: {roof_type}.")

    def set_doors(self, count: int):
        self._specification.add_detail(f"Number of interior and exterior doors: {count}.")

    def set_pool(self, has_pool: bool):
        status = "Present" if has_pool else "Absent"
        self._specification.add_detail(f"Pool: {status}.")

    def set_garage(self, has_garage: bool):
        status = "Present" if has_garage else "Absent"
        self._specification.add_detail(f"Garage: {status}.")

    def get_result(self) -> HouseSpecification:
        product = self._specification
        self.reset()
        return product

class Director:
    def construct_luxury_villa(self, builder: Builder):
        builder.reset()
        builder.set_walls("Marble and Brick")
        builder.set_roof("Ceramic Tiles")
        builder.set_doors(15)
        builder.set_pool(True)
        builder.set_garage(True)

    def construct_simple_cottage(self, builder: Builder):
        builder.reset()
        builder.set_walls("Wood")
        builder.set_roof("Slate")
        builder.set_doors(4)
        builder.set_pool(False)
        builder.set_garage(False)

director = Director()

print("=== Creating a Luxury Villa ===")
house_builder = HouseBuilder()
director.construct_luxury_villa(house_builder)
villa = house_builder.get_result()
print(villa)

spec_builder = HouseSpecificationBuilder()
director.construct_luxury_villa(spec_builder)
villa_spec = spec_builder.get_result()
print(f"\n{villa_spec}")

print("=== Creating a Simple Cottage ===")
director.construct_simple_cottage(house_builder)
cottage = house_builder.get_result()
print(cottage)

director.construct_simple_cottage(spec_builder)
cottage_spec = spec_builder.get_result()
print(f"\n{cottage_spec}")