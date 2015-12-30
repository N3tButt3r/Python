# Archivo: Paradoja Monos.py
# Autor: Genís Martínez 
# Fecha: 02 de Diciembre de 2015
# Descripción: Ejercicio probabilidad infinita. 

import string
import random

search = input('¿Que palabra quieres buscar? "Sin acentos" ')
rango1 = int(input('¿Cuantos carácteres quieres que tenga cada línea?'))
rango = range(rango1)
num = ''
line = 1
while not search in num:
     num=''.join(random.choice(string.ascii_letters) for _ in rango )
     print ('<',line,'>', num)
     line = line + 1

I =  num.index(search)
F =  I + len(search)
T =  len(num)
print ('->', line, num)
print ("Encontró",search,"en la línea", line,"después de", rango1 * line ,' carácteres:', num[0:I], "{",search,"}", num[F:T])
