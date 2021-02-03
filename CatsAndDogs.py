#make a simple exp of OOP


class Dog:
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed
  def bark(self):
      print("Woof!")
  def sayBreed(self):
      self.bark()
      print("I'm a " +  self.breed +  ".")
  def sayName(self):
      self.bark()
      print("My name is " + self.name)





class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def meow():
      print("Meeow.")



Dexter = Dog("Dexter", 3, "bernedoodle")




print(Dexter) # example of how objects are reference types, maybe  go into





Dexter.bark()
Dexter.sayBreed()
Dexter.sayName()
