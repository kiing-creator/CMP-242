class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.horsepower} HP"


class Wheel:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size}-inch wheel"


class Car:
    def __init__(self, make, brand, horsepower, wheel_size):
        self.make = make
        self.brand = brand
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def get_car(self):
        wheel_sizes = ", ".join(str(wheel) for wheel in self.wheels)
        return (
            f"Make: {self.make}, Brand: {self.brand}, "
            f"Engine: {self.engine}, Wheels: [{wheel_sizes}]"
        )


# Example usage
my_car = Car("Toyota", "Corolla", 132, 16)
print(my_car.get_car())
