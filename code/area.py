def area_square():
  s = float(input("Enter the side of square: "))
  area = s ** 2
  return area

def area_retangle():
  l = float(input("Enter the length: "))
  b = float(input("Enter the Breadth: "))
  area = l * b
  return area

def area_circle():
  r = float(input("Enter Radius: "))
  pi = 3.14159
  area = pi * r ** 2
  return area

def display_area():
  shape = input("Enter the name of the shape (one of square, rectangle or circle): ")
  shape = shape.lower()

  if (shape == "square"):
      print("Area of square = ", area_square())
  elif (shape == "rectangle"):
      print("area of rectangle: ", area_retangle())
  elif (shape == "circle"):
      print("area of circle: ", area_circle())
  else:
      print("Shape not availble")

display_area()