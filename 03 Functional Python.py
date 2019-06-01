#%% Ejercicio 1:
#   Dados 3 enteros (X, Y, Z) que representan las dimensiones de un tetraedro,
#   y dado un número N; imprima todas las posibles coordenadas por (i, j, k) en
#   una cuadrícula tridimensional donde la suma de i + j + k no sea igual a N,
#   de modo que: 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z.

X, Y, Z = 1, 2, 3
N = 4

print([(i, j, k) for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if (i + j + k != N)])

#%% Ejercicio 2:
#   Dado un string que contiene números enteros separados por espacio,
#   determine los números de la lista que son números “palíndromos”.

nmbs = "101 234 454 666 325 797"
nmbs = ["".join(i) for i in list(filter(lambda x: x == x[::-1], list(map(list, nmbs.split(" ")))))]
print(f"En la lista, los números {nmbs} son palíndromos.")

#%% Ejercicio 3:
#   Dada la siguiente lista de strings cuente cuántas veces se repite la 
#   palabra “Python” en toda la lista.

lista = ["We are learning Python", "Functional programming in Python", 
         "What are this Python functions for?", "Do we really need Python?", 
         "Python rulez!"]

n = sum(list(map(lambda w: "Python" in w, lista)))
print(f"La palabra 'Python' aparece {n} veces en la lista.")

#%% Ejercicio 4:
#   ¿Cuál es la suma de los primeros 50 números positivos cuyo cuadrado es
#   divisible por 5?.

n = sum(list(filter(lambda x: (x**2)%5 == 0, range(1,1000)))[:50])
print(f"La suma de los primeros 50 números positivos es {n}.")