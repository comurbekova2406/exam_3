class Rectangle:

    def __init__(self, a, b) -> None:
        self.a = int(a)
        self.b = int(b)

    @property
    def fact(self):
        return 'I am figure and have a,b'

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return (self.a + self.b)*2


f1 = Rectangle(5, 3)
print(f1.fact)
print(f1.calculate_perimeter())
print(f1.calculate_area())

