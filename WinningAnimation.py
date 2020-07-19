import turtle
import time
import random 


def WinningAnimation():
     WindowAnimation = turtle.Screen()
     WindowAnimation.bgcolor("black")
     WindowAnimation.bgpic("5.png")
     WindowAnimation.title("You Won Animation")
     WindowAnimation.tracer(0)

     #Create the avatars and store them in a list
     avatars = []

     

     for i in range(15):
          avatars.append(turtle.Turtle())


     WindowAnimation.register_shape("avatarKnight.gif")
     WindowAnimation.register_shape("avatarCannibal.gif")
     WindowAnimation.register_shape("avatarLumberjack.gif")
     WindowAnimation.register_shape("avatarArcher.gif")
     
     imgs = ["avatarLumberjack.gif","avatarCannibal.gif","avatarKnight.gif","avatarArcher.gif"]
     pen = turtle.Turtle()
     pen.hideturtle()
     pen.speed(0)
     pen.shape("square")
     pen.color("black")
     pen.penup()
     pen.goto(0,150)
     font = ("Fixedsys",80,"normal")
     pen.write("YOU WON! :)",font=font,align="center")

                
     for avatar in avatars:
          avatar.shape(random.choice(imgs))
          avatar.penup()
          avatar.speed(0)#speed of the movement
          X = random.randint(-290,290)
          Y = random.randint(200,400)
          avatar.goto(X,Y)#place where it starts
          avatar.dy = 0
          avatar.dx = random.randint(-3,3) #to move from left to right 
          avatar.da = random.randint(-5,5)
          gravedad = 0.1

     while True:
          time.sleep(0.01)
               
          WindowAnimation.update()

          for avatar in avatars:
               avatar.rt(avatar.da)
               avatar.dy -= gravedad 
               avatar.sety(avatar.ycor() + avatar.dy)

               avatar.setx(avatar.xcor() + avatar.dx)
               #check for borderlines
               if avatar.xcor() > 330: 
                    avatar.dx *= -1
               if avatar.xcor() < -330:
                    avatar.dx *= -1
               #bounces
               if avatar.ycor() < -330:
                    avatar.dy *= -1 

               


     WindowAnimation.mainloop()


WinningAnimation()



     
     
