# Assignment/exercise 1 (15 minutes)
# Write a class named Person with instance variables like id, name, birth_year, salary!
# • Use constructor to set the values of the variables
# • Create descructor that display a message: “Goodbye, name”
# • Create a Person instance named p with the following data: id: 2023, name:
# ‘Joe White’, birth_year: 1995, salary: 5600

class Person:
    def __init__(self, id, name, birth_year, salary):
        self._id = id                       #protected
        self._name = name
        self._birth_year = birth_year
        self._salary = salary

    def set_salary(self, value):
        self._salary = value

    def get_name(self):
        return self._name
    def get_salary(self):
        return self._salary
    '''def __del__(self):
        print(f'Goodbye, {self._name}')'''

p = Person(2023, 'Joe', 1995, 1200)
p.set_salary(6000)
print(p.get_name(), p.get_salary())

        

# Assignment/exercise 2 (15 minutes)
# Add the following methods to the Person class to set/get the related variable’s value
# • set_salary
# • get_name
# Then use @property decorator to set/get the value of birth_year!




# Assignment/exercise 3 (30 minutes)
# Inherit a new class from the Person class named Student!
# • Add two new instance variables to the Student class: neptuncode and
# semester
# • Create constructor in Student class invoking the constructor of the parent
# class
# • Create a method that returns the student’s age in years
# • Create a method to print Student instances
# • Test the Student class by creating at least one instance!

class Student(Person):
    def __init__(self, id, name, birth_year, salary, neptuncode, semester):
        super().__init__(id, name, birth_year, salary)
        self.__neptuncode = neptuncode
        self.__semester = semester

    def __str__(self):
        return f'id: {self.id} name: {self._name}'
    
    
s = Student(100,'Black', 2000, 5000, 'AEKROE', 1)


# Assignment/exercise 4 (30 minutes)
# Create a new class named Shape. Include (empty) methods to calculate its area and
# perimeter. Store the approximate value of PI in a hidden class variable.
# • Create subclasses called Rectangle and Circle. Override the area and
# perimeter methods using the appropriate parameters and formula!
# • Modify the Rectangle class that automatically creates a square if only the
# width parameter is provided!
# • Test the classes by creating instances and calling methods!

class Shape:
    _PI = 3.14
    def perimeter(self):
        pass
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height = None):
        if height is None:
            self.__width = width
            self.__height = width
        else:
            self.__width = width
            self.__height = height
    def perimeter(self):
        return 2*(self.__width + self.__height)
    def area (self):
        return self.__width* self.__height
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    def perimeter(self):
        return 2*self.__radius*Shape._PI
    def area(self):
        return self.__radius**2*Shape._PI
        
    
s = Rectangle(3, 100)
print(s.perimeter())
print(s.area())
c = Circle(3)
print(c.perimeter())
print(c.area())
# Assignment/exercise 5 (40 minutes)
# Create a class Fraction that utilizes operator overloading to implement the four basic
# operations (+, -, *, /) for fractions!
# • Override the __str__() method to define a string representation of the
# Fraction objects
# • Modify the Fraction class: if only the numerator is provided then the
# denominator will default to 1 (integer)
# • Test the Fraction class as follow:
# o f1 = Fraction(1, 2)
# o f2 = Fraction(3, 4)
# o f3 = Fraction(4)
# o print(f1 + f2) # 5/4
# o print(f1 – f2) #-1/4
# o print(f1*f2) # 3/8
# o print(f1/f2) # 2/3
# o print(f3-f1) #7/2



# Homework:
# Add new methods to the Fraction class created in seminar to implement the following
# operations: ==, <, >
# In each case, use operator overloading!