class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Ділення на нуль неможливе!")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("2 + 3 =", calc.add(2, 3))  
    print("10 / 2 =", calc.divide(10, 2))