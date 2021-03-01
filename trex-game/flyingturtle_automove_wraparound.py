import turtle

class FlyingTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.shapesize(2)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = -1
        self.ybot = -200
        self.automove = True
        self.wraparound = True
        self.move()
        
    def move(self):
        nx = self.xcor() + self.vx
        ny = self.ycor() + self.vy

        if ny < self.ybot:
            ny = self.ybot
            self.vy = 0

        if self.wraparound == True:
            screen_width = self.getscreen().window_width()
            if nx > screen_width/2:
                nx = - screen_width/2
                self.penup()
            elif nx < - screen_width/2:
                nx = screen_width/2
                self.penup()
            
        self.getscreen().tracer(0)
        self.goto( nx, ny )
        self.pendown()
        self.getscreen().update()
        self.vx += self.ax
        self.vy += self.ay
        if self.automove == True:
            self.getscreen().ontimer(self.move, int(1000/60))
        
    def jump(self):
        self.vy += 10

    def run_right(self):
        self.vx += 1

    def run_left(self):
        self.vx -= 1

tina = FlyingTurtle()
tina.getscreen().onkey(tina.jump, "space")
tina.getscreen().onkey(tina.run_right, "Right")
tina.getscreen().onkey(tina.run_left, "Left")
tina.getscreen().listen()
tina.getscreen().mainloop()

