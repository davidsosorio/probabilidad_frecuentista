import random

n = int(input('Cuátas muestras quiéres tomar?: '))
n_Aciertos = 0

A = [2, 4, 6]

for i in range(1, n+1):
    x = random.randint(1,6)
    if x in A:
        n_Aciertos += 1
    else:
        continue

probabilidad = n_Aciertos / n

print('Trataremos de comprobar la probabilidad de que, al lanzar un dado, la mitad de las veces cae par')
print('La probabiliad es: {}'.format(probabilidad)) #Entre más sean las muestras, más se acerca a la probabilidad.
