# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 01:07:05 2021

@author: Martha
"""

from sympy import *

MostrarTexto=input('Ingrese funcion: ')
punto_a=float(input('Ingrese extremo inferior del intervalo cerrado: '))
punto_b=float(input('Ingrese extremo superior del intervalo cerrado: '))
error=float(input('Ingrese porcentaje de error: '))
f=sympify(MostrarTexto)

if f.subs('x',punto_a)*f.subs('x',punto_b)<0:
    xrant=punto_a   #xrant: raiz antigua
    xr=punto_a-(f.subs('x',punto_a)*(punto_b-punto_a)/(f.subs('x',punto_b)-f.subs('x',punto_a)))   #xr: raiz nueva
    ea=abs((xr-xrant)/xr)*100
    salir=0
    while(ea>error and salir==0):
        if f.subs('x',punto_a)*f.subs('x',xr)<0:
            xb=xr   
        elif f.subs('x',xr)*f.subs('x',punto_b)<0:
            xa=xr           
        else:           
            salir=1
            punto_a=xr
            punto_b=xr
        xrant=xr
        xr=punto_a-(f.subs('x',punto_a)*(punto_b-punto_a)/(f.subs('x',punto_b)-f.subs('x',punto_a)))
        ea=abs((xr-xrant)/xr)*100
    print('La raiz aproximada es: ',xr)
else:
    print('En el intervalo \"No hay Raiz\".')