import turtle

turtle.shape("turtle") #Tortuga

turtle.color("red","blue")
turtle.speed('normal')

for j in range(10):
    turtle.right(36)
    turtle.pendown()
    if j%2==0:
        turtle.begin_fill()
        for i in range(5):
                turtle.forward(100)
                turtle.left(72)
        turtle.penup()
        turtle.end_fill()
    else:    
        for i in range(5):
                turtle.forward(100)
                turtle.left(72)
    

turtle.hideturtle()

turtle.exitonclick() 