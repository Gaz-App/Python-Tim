
name = 'gaz'
age = 50

#print(name + " edad :" + age)
# pero si conacteno un valor entero :

#print(name + " edad :" + age)
# va a marcar un error: TypeError: can only concatenate str (not "int") to str


print(name + f" Tiene una edad : {age} años")

print ('-------------------->')

print(f"Pi is aprox : {22/7:12.50f}")

# Other way:

pi = 22/7

print (f"Pi es aprox : {pi:12.50f}")