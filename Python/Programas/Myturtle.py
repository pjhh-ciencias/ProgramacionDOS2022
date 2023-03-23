import turtle
#-----------------------------------------------------------------
#                Definir imagen del puntero
#-----------------------------------------------------------------
turtle.shape("turtle") #Tortuga
#turtle.shape("arrow") #flecha
#turtle.shape("circle") #Circulo
#turtle.shape("square") #Cuadrado
#turtle.shape("triangle") #Triangulo

#-----------------------------------------------------------------
#              Definiendo color de puntero y de trazo
#-----------------------------------------------------------------
turtle.color("green","blue")

#-----------------------------------------------------------------
#                           Movimientos
#-----------------------------------------------------------------
turtle.speed('slowest') # fastest,fast,normal,slow, slowest
turtle.forward(100) #Hacia adelante
turtle.backward(50) #Hacia atras
turtle.forward(50) #Hacia adelante
 
turtle.left(90) #Gira 90º en sentido contrario a las manecillas del reloj
turtle.forward(100) #Hacia adelante

turtle.right(90) #Gira 90º en el sentido de las manecillas del reloj
turtle.forward(100) 

turtle.right(90)
turtle.forward(200) 

turtle.right(90)
turtle.forward(200)

turtle.right(90)
turtle.forward(100)


turtle.onclick(None)

#-----------------------------------------------------------------
#                       Formas rellenas
#-----------------------------------------------------------------

turtle.clear()

turtle.begin_fill() #Instrucción introducida antes del código que dibuja la forma que se desea rellenar.

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.end_fill() #Instrucción agregada al final del código que dibuja la forma que se desea rellenar.

# turtle.pendown() 
# turtle.begin_fill()


# #turtle.left(90)
# #turtle.forward(100)




turtle.exitonclick() #



#-----------------------------------------------------------------
#                       Otras funciones
#-----------------------------------------------------------------

turtle.stamp()

#-----------------------------------------------------------------
#                    Comportamiento del lapiz
#-----------------------------------------------------------------

turtle.pendown() #Baja el lápiz – dibuja mientras se mueve.
turtle.penup() #Levanta el lápiz – no dibuja mientras se mueve.