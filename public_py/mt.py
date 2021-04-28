from random import randrange, seed

seed(11)
randrange(0, 11)

notas_matematicas = []
for notas in range(8):
    notas_matematicas.append(randrange(0, 11))

print(notas_matematicas)

import matplotlib.pyplot as plt

x = list(range(1, 9))
y = notas_matematicas

plt.plot(x, y, marker= 'o')
plt.title('Notas Matemáticas')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
