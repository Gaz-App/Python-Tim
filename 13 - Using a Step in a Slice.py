import random

time = random.randint(1, 1000)
print(time)

print('------------------>')
print('Python’s slice notation')
lista = "francisco gaz"
cadena = list(lista)

print('[start:stop:step]')
print(cadena)
print(cadena[0:3])
print(cadena[-6:])  # imprime -6 posiciones empezando desde el final
print(cadena[::2])  # imprime cada dos segmentos, empezando desde el index 0
print(cadena[::-1])  # imprime en sentido contrario (reverse) toda las cadena.
print(cadena[13:9:-1])  # empieza en el index 12(13), para en el index 9  y hace paso reverse -1
print(cadena[10:13])
print("")
print(cadena[10:13:2])  # emieza en el index 11(10), despues para en el index 13
# recorre hacia atras cada 2 posiciones,
# empezando por la ultima.
"""
Cortar una lista no es destructivo, ya que extraer
los objetos de una lista existente no la alteran; los datos originales permanecen
intacto.
"""
print('------------------>')
a = "Norwegian Blue"

print(a[0:6:2])  # STAR = 0: = N / STOP = :6= Norwegi
# STEP REVERSE :2 A LA IZQ = Nre

print(a[0:6:3])  # Nw

print(a[0:6:1])  # Norweg

print('------------------>')
b = "012345678901234"
print(b[0:6:2])
print(b[0:6:3])
print(b[0:6:1])

c = "9,333,444,555,666,777,888,999,000"
print(c[1::4])

d = "9,333;444,555;666,777;888,999:000"
separete = d[1::4]
print(separete)

join = "".join(char if char not in separete
               else " " for char in d).split()

print([int(val) for val in join])

print("----------------------------------->")
txt = "welcome to_the world of Python"

x = txt.split()

print(x)
"""
-Divide una cadena en una lista donde cada palabra es un elemento de lista.
- El método divide una cadena en una lista.split()
Puede especificar el separador, el separador predeterminado es cualquier espacio en blanco
"""

print("----------------------------------->")
"""
- Combina todos los elementos de una tupla en una cadena, utilizando un 
carácter - como separado.

-El método toma todos los elementos de un objeto iterable y los combina en una cadena.join()
Se debe especificar una cadena como separador.

"""
myTuple = ("John", "Peter", "Vicky")

z = "-".join(myTuple)
y = "".join(myTuple)

print(z)
print(y)
