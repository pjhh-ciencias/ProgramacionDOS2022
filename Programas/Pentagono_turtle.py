import turtle

turtle.shape("turtle") #Tortuga


turtle.color("blue")
turtle.speed('slowest')

turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.left(72)
turtle.end_fill()

turtle.exitonclick() 