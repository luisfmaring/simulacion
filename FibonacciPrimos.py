#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 07:10:18 2019

@author: luisfelipemaringiraldo
"""

import matplotlib.pyplot as plt
from datetime import datetime, date, time, timedelta


def fibonacci(n):
    return int((pow( (1 + pow(5,0.5))/2, n) -  pow( (1 - pow(5,0.5))/2, n))/pow(5,0.5))

def fibonacciC(a,b,n):
    for i in range(n): 
            c = a + b
            a = b 
            b = c
    return b


def esPrimo(n):

    if(n== 2 or n==4):
        return True

    if(n % 2 > 0):
        j = 0
        hasta = int(pow(n,0.5))
        for i in range(2,hasta + 1):
            if(n % i == 0):
                j = j + 1
        if(j == 0):
            return True

    return False


cuenta = 0
i = 2
nuemeroActual = 0
tope = 1474
fhand = open('tiempos.txt', 'w')

fechaInicial , fechaFinal = datetime.now(), datetime.now() + timedelta(hours=1)
while  True:
    if(esPrimo(i)):
        if(i <= 1474):
            f = fibonacci(i)
        else:
            f = fibonacciC(fibonacci(tope-1),fibonacci(tope), i - tope)
        cuenta = cuenta + 1
        fhand.write( str(datetime.now() - fechaInicial) + '\t' + str(i) + '\n')
    i = i + 1
    if(datetime.now() >= fechaFinal):
        break
    
fhand.close()



x,y=[],[]
with open("tiempos.txt") as fichero:
    for linea in fichero:
        strDato = str.replace(str.replace(linea,'\t',' '),'\n','').split(' ')
        fecha = strDato[0].split(':')
        n = int(strDato[1])
        ms = int(fecha[0]) * 3.6e+6 + int(fecha[1])*60000 + float(fecha[2])*1000
        x.append(n)
        y.append(ms)

plt.scatter(x, y, s=20)
plt.autoscale(enable=True, axis='both', tight=None)
plt.show()