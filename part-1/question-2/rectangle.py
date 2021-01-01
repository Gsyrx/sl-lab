class Rectangle:
  def __init__(self):
    self.l = int(input("Enter the length : "))
    self.b = int(input("Enter the breadth : "))
  def area(self):
    print("The area of the rectangle = ", self.l * self.b)

rect = Rectangle()
rect.area()