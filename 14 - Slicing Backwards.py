#Cortar al revés

letters = "abcdefghijklmnopqrstvwyz"   # 23 letras

backwards = letters[23:0:-1]
# empieza en la ultima, letra, para aqui y empieza su recorrido de reversa de 1 en 1
# se pierde la letra por el stop 0
print(backwards)

backwards2 = letters[23::-1]
#va hacia al final, NO PARA, y recorre en -1
print (backwards2)