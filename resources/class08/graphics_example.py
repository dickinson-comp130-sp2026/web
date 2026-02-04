import graphics as gr
window_size = 300
window = gr.GraphWin("graphics window with origin at bottom left", window_size, window_size)
window.setCoords(0, 0, window_size, window_size)

p = gr.Point(100, 60)
c = gr.Circle(p, 25)

c.draw(window)

window.getMouse() # pause for click in window
window.close()
