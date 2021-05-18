class Shapes:  # Initializing the attributes #Defining the superclass
    def __init__(self, side, type, size, name):
        self.side = side
        self.type = type
        self.size = size
        self.name = name

    def area(self):
        print(
            "I am a" + self.name + "\n" + "I have" + self.side + "\n" + "I am a" + self.type + "\n" + "I have a size of" + self.size)


obj_shape = Shapes("shape", "4", "polygon", "14 cm")
obj_shape.area()


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * self.radius * self.radius
        return result


obj_coin = Circle(5)
print(obj_coin.area())


# Triangle
class Triangle(Shapes):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        x = 6
        y = 6
        result = 0.5 * x * y
        return result


obj_pyramid = Triangle("sdsds", "dfsdf")
print(obj_pyramid.area())


# Square
class Square(Shapes):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        result = 0.5 * (self.side1 * self.side2)
        return result

obj_laptop = Square(5, 10)
print(obj_laptop.area())

#rectangle
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        return result

obj_rect = Square(5, 10)
print(obj_rect.area())
