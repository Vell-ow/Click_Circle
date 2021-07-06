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
# 3. Define the function moveTo, a graphics object that supports the 
# getCenter method, and newCenter, a Point. The function moves the 
# specified shape so that newCenter is its center.
# 3. Create a counted loop that allows the user to click 10 times.
# Each time the user clicks, the circle is moved where the user clicked.
# 4. Change the position of the circle based on the new x and y 
# coordinates retrieved from each click
#
#
#
# import the necessary python libraries

def main():    

  c = Circle(Point(20, 20), 10)
  # changes the position of the circle based on its center.
  def moveTo(c, newCenter):
    c.getCenter()
    c.move(xCo, yCo)
    moveTo()
  # Print a message to the screen    
  print("Hello!")        
  win = GraphWin("Click Me Ten Times!", 600, 600)
  init = win.getMouse()
  c.draw(win)
  for i in range (10):
    q = win.getMouse()
    xCo = q.getX() # retrieve the x-coordinate for the new point
    yCo = q.getY() # retrieve the y-coordinate for the new point
    moveTo(c, Point(xCo, yCo))
  win.close()    # Close window when done
main()