from graphics import *
# File Name:     Homework6_ExtraCredit.py
# Programmer:    Andrew Coviello
# Date:          Jul. 5, 2021
#
# Problem Statement: Draw a circle, then allow the user to click up to 10
# times to move the circle to a new location equal to the coordinates of
# the latest click.
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Draw a circle
# 3. Create a counted loop that allows the user to click 10 times
# 4. Change the position of the circle based on the new x and y 
# coordinates retrieved from each click
#
#
#
# import the necessary python libraries

def main():    

  # changes the position of the circle based on its center.
  def moveTo():

    moveTo()
  # Print a message to the screen    
  print("Hello!")        
  win = GraphWin("Click Me Ten Times!", 600, 600)
  init = win.getMouse()
  c = Circle(Point(init.getX(),init.getY()), 25)
  for i in range (10):
    q = win.getMouse()
    xCo = q.getX() # retrieve the x-coordinate for the new point
    yCo = q.getY() # retrieve the y-coordinate for the new point
    moveTo(c, Point(xCo, yCo))
  win.close()    # Close window when done
main()