for i in range(1, 13):
    print("No. {0} cuadrado es: {1} el cubo es: {2}".format(i, i ** 2, i ** 3))

print('alineacion de caracteres----------------------------------->')

for i in range(1, 13):
    print("No. {0:2} cuadrado es: {1:3}  el cubo es: {2:4}".format(i, i ** 2, i ** 3))

print('alineacion de caracteres----------------------------------->')
for i in range(1, 13):
    print("No. {0:2} cuadrado es: {1:<3}  el cubo es: {2:<4}".format(i, i ** 2, i ** 3))
    #{2:^4}

print('formato de impresión de Numeros----------------------------------->')

print ("Pi es aprox: {0:12}".format(22/7))
print ("Pi es aprox: {0:12f}".format(22/7))
print ("Pi es aprox: {0:12.50f}".format(22/7))
print ("Pi es aprox: {0:52.50f}".format(22/7))
print ("Pi es aprox: {0:62.50f}".format(22/7))
print ("Pi es aprox: {0:72.50f}".format(22/7))
print ("Pi es aprox: {0:<72.50f}".format(22/7))