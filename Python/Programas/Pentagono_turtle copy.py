import turtle

turtle.shape("turtle") #Tortuga

turtle.color("blue")
turtle.speed('fast')

for j in range(10):
    turtle.right(36)
    for i in range(5):
        turtle.forward(100)
        turtle.left(72)

turtle.exitonclick() 