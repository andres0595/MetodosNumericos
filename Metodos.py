import math


e=float(input("Digite rugosidad e(m): "))
D=float(input("Digite diametro D(m): "))
R=float(input("Digite reynlods:  "))

# Ecuacion de colebrook white
def f(x):
    return 1/x**0.5+2*math.log10((e/D)/3.7+2.51/(R*x**0.5))

# Derivada de la funcion
def DF(x):
    return -0.5*x**-1.5+2*(-2.51*x**-1.5/(2*R))*math.log10(2.7182)/((e/D)/3.7+2.51/(R*x*0.5))

x0=0.015
i=1
for iteracion in range (1,11):
    x1=x0-f(x0)/DF(x0)
    x0=x1
    print("iteracion", i,x0)
    i=i+1
