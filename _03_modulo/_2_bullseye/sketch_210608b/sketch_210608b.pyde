def setup():
    # Set the size of your sketch
    size(800,800)
    
    pass
    
def draw():
    w = 400
    h = 400
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(3):
        w -= 100
        h -= 100
        ellipse(400,400,h,w)
        fill(255,w,h)
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
