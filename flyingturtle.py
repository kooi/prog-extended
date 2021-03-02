import turtle

class FlyingTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.shapesize(3)
        self.vy = 0
        self.ay = -1
        self.move()

    def move(self):
        ny = self.ycor() + self.vy
        self.goto(0, ny)
        self.getscreen().ontimer(self.move, int(1000/60))
        self.vy = self.vy + self.ay
        
    def jump(self):
        self.vy = self.vy + 10

tina = FlyingTurtle()

tina.getscreen().onkey(tina.jump, "space")
tina.getscreen().listen()

