import turtle

n=int(input('Ingresa un número entero mayor que 2: '))

while n <=2:
    print('El número debe ser entero mayor que 2.')
    n=int(input('Ingresa un número entero mayor que 2: '))

longitud=100
giro=360/n

turtle.shape("turtle")
turtle.color("black","blue")
turtle.speed("normal")

for j in range(60):
    turtle.left(5)
    for i in range(n):
        turtle.forward(longitud)
        turtle.left(giro)

turtle.hideturtle()
turtle.exitonclick()





