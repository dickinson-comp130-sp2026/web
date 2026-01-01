import graphics

# Construct a point and a circle
p = graphics.Point(50, 100)
c = graphics.Circle(p, 25)

# Construct the graphics window
win = graphics.GraphWin("Graphics Demo", 640, 480)

# Draw the circle
c.draw(win)

# Pause for a mouse click in the window, then close the window.
win.getMouse()
win.close()
