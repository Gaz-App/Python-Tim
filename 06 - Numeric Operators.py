a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 Integer divison, rounded down towards minus infinity "DIVISON ENTERA"
print(a % b)  # 0 modulo: the remainder after integer divison

print("---------------->")

for i in range(0, 4):
    print(i)

print("---------------->")
for i in range(a // b): # Resultado de la division es en numero entero 4
    print(i)

print("---------------->")
for i in range(a / b):  # Daria error por que el resultado es float : 4.0
    print(i)            # TypeError: 'float' object cannot be interpreted as an integer
