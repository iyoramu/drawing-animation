import turtle
from sketchpy import canvas

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Load and draw the image
image = canvas.sketch_from_image("ironman.jpg")
image.draw()
