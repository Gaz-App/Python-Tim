"""
Python usa formato de cadena de estilo C para crear cadenas nuevas con formato.
El operador "%" se utiliza para formatear un conjunto de variables encerradas en una
"tupla" (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto
normal junto con "especificadores de argumentos",
símbolos especiales como "% s" y "% d"
"""
age = 50

print('My age is %d years' % age)

print('-------------------->')
year = 'Años'
mounth = 'Meses'
print('Mi edad es %d %s y %d %s ' % (age, year, 7, mounth))

pi = 22/7

print ("Pi es aprox: %f " %pi)
print ("Pi es aprox: %50.50f " %pi)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])


flower1 = "blue violet"
print('violet' in flower1)


flower = "rose"
colour = "red"
print ("the {0} is {1}".format(flower,colour))


@ ESTE ES EL MASTER
# ESTE ES COMENTARIO!!!
# CESBA VIERNES 15 DE OCT 2021

