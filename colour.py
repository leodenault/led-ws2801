class Colour:
  WHITE = Colour(255, 255, 255, "White")
  RED = Colour(255, 0, 0, "Red")
  GREEN = Colour(0, 255, 0, "Green")
  BLUE = Colour(0, 0, 255, "Blue")
  BLACK = Colour(0, 0, 0, "Black")
  GOLD = Colour(255, 125, 0, "Gold")

  def __init__(self, r, g, b, name=""):
    self.r = r
    self.g = g
    self.b = b
    self.name = name
  
  def add(self, other):
    return Colour(self.r + other.r, self.g + other.g, self.b + other.b)
  
  def multiply(self, factor):
    return Colour(int(self.r * factor), int(self.g * factor), int(self.b * factor))
  
  def __str__(self):
    if self.name:
      return self.name
    else:
      return "({0}, {1}, {2})".format(self.r, self.g, self.b)
