from turtle import Turtle, done
import random

# 1. Drawing a Square
# Task: Create a function that draws a square. The turtle should move forward by 100 units
#       for each side and turn right by 90 degrees after drawing each side.

def draw_square(t):
   for i in range (4):
      t.forward(100)
      t.right(90)

# 2. Drawing a Circle
# Task: Create a function that draws a circle with a radius of 50 units.

def draw_circle(t):
   t.circle(radius = 50)

# 3. Drawing a Triangle
# Task: Create a function that draws an equilateral triangle. The turtle should move forward
#       by 100 units for each side and turn right by 120 degrees after drawing each side.
#edit it 
   
def draw_triangle(t):
   for i in range (3):
      t.forward(100)
      t.left(120)

# 4. Using Colors
# Task: Create a function that draws a red square. Use the turtle's fill functionality to fill
#       the square with red color.
def red_square(t):
   t.fillcolor('red')
   t.begin_fill()
   for i in range (4):
      t.forward(100)
      t.right(90)
   t.end_fill()

# 5. Drawing a Star
# Task: Create a function that draws a five-pointed star. The turtle should move forward
#       by 150 units for each line and turn right by 144 degrees.

def star(t):
   for i in range(5):
      t.forward(150)
      t.right(144)

# 6. Setting Position
# Task: Create a function that moves the turtle to a specific position (e.g., -100, 50) without
#       drawing anything, then draws a square starting from that position.

def position(t, x, y):
   t.penup()
   t.goto(x,y)
   t.pendown()
   draw_square(t)


# 7. Adjusting Speed
# Task: Create a function that draws a large square (200 units per side) at the slowest speed
#       using the turtle's speed setting.

def slow(t):
   t.speed(1)
   draw_square(t)

# 8. Measuring Distance
# Task: Create a function that moves the turtle to a specific position (e.g., 100, 100) and
#       measures the distance from its current position to the origin (0, 0).

def howfar(t, x, y):
   t.penup()
   t.goto(x,y)
   print(t.distance(0,0))

# 9. Clearing and Resetting
# Task: Create a function that draws something (e.g., two connected lines) and then clears
#       the drawing, resetting the turtle to its initial state.
   
def drawdelete(t):
   for i in range(2):
      t.forward(100)
      t.right(90)
   t.clear()
   t.penup()
   t.goto(0,0)


# 10. Creating a BlueTurtle
# Task: Create a new class called BlueTurtle that inherits from the Turtle class. Override the
#       color method to always set the pen color to blue, regardless of the input.

class BlueTurtle(Turtle):
   def color(self, *args):
      super().color('blue')

# 11. BlueTurtle Drawing a Spiral
# Task: Use the BlueTurtle class to draw a spiral pattern. The turtle should move forward by
#       an increasing distance and turn right by 30 degrees at each step.
      
def spiral(t):
   colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'grey', 'yellow']
   t.speed(0)
   for i in range(10000):
      t.color(colors[i%8])
      t.forward(i/10)
      t.right(30)

# 12. Randomized BlueTurtle
# Task: Create a function that uses the BlueTurtle class to draw random lines on the canvas.
#       The starting position, direction, and line length should be randomized.

if __name__ == '__main__':
   t2 = BlueTurtle()
   spiral(t2)
   done()