# Programa para calcular la suma de los primeros n-numeros naturales.

n=int(input('¿Hasta que nùmero deseas sumar?'))

sum=0
for i in range(1,n+1):
    sum=sum+i


print('La suma de los primeros {} nùmeros es {}'.format(n,sum))

input()
input()
