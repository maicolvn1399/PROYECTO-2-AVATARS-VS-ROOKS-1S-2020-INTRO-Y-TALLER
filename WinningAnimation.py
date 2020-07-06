import turtle
import os,random,time

#Variables for display
animationWindow = turtle.Screen()
animationWindow.title("You Won!!!")
animationWindow.bgcolor("green")
animationWindow.bgpic("5.png")
animationWindow.setup(width=800,height=600)
animationWindow.tracer(0)
animationWindow.register_shape("diamond1.gif")
animationWindow.register_shape("diamond2.gif")
animationWindow.register_shape("diamond3.gif")

diamondShapes = ["diamond1.gif","diamond2.gif","diamond3.gif"]

#Create a list of diamonds
diamonds = []

#Add the diamonds
for i in range(50):
    diamond = turtle.Turtle()
    diamond.speed(0)
    diamond.shape(random.choice(diamondShapes))
    diamond.color("blue")
    diamond.penup()
    diamond.goto(0,250)
    diamond.speed = random.randint(1,4)
    diamonds.append(diamond)


#Pen to write on screen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.goto(0,150)
font = ("Fixedsys",80,"normal")
pen.write("YOU WON!!!",font=font,align="center")

#Mainloop for the animation
while True:
    animationWindow.update()
    #Move the diamond
    for diamond in diamonds:
        y = diamond.ycor()
        y -= diamond.speed
        diamond.sety(y)
        #Check if off the screen
        if y < -300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            diamond.goto(x,y)












animationWindow.mainloop()
