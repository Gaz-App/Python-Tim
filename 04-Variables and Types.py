# Las variables son sensibles a Mayusculas y Minisculas
# Pueden contenr letras, numeros y underscore...No puden empezar con numeros.
# No pueden utilzarse palabras reservadas.

saludo = 'Hola'
Saludo = 'HOLA'

print(saludo)
print('--------------')
print(Saludo)
print('--------------')
edad = 50
print(edad)
print(type(edad))
print('--------------')
print(type(edad))
print(type(saludo))
print('--------------')
# se puede reasignar el tipo de variable.
edad = '50 años'
print(edad)
print(type(edad))

print('--------------')

name = 'gaz'
age = 50

print(name + " edad :")
# pero si conacteno un valor entero :

#print(name + " edad :" + age)
# va a marcar un error: TypeError: can only concatenate str (not "int") to str
