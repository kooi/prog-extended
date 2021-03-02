import turtle

class FlyingTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.shapesize(3)
        self.vy = 0
        self.vx = 5
        self.ay = -1
        self.bottom = 0
        self.right = 200
        self.left = -200
        self.move()

    def move(self):
        nx = self.xcor() + self.vx
        ny = self.ycor() + self.vy
        
        if ny < self.bottom:
            ny = self.bottom
            self.vy = 0
            
        if nx > self.right:
            nx = self.left
        
        self.goto(nx, ny)
        self.getscreen().ontimer(self.move, int(1000/60))
        self.vy = self.vy + self.ay
        
    def jump(self):
        self.vy = self.vy + 10

tina = FlyingTurtle()

tina.getscreen().onkey(tina.jump, "space")
tina.getscreen().listen()

