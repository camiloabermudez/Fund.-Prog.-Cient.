#%% Ejercicio 1: Convolución unidimensional entre dos polinomios.

from scipy.ndimage import interpolation as nt
from matplotlib import pyplot as plt
import numpy as np

P = lambda x: 2*(x**3) + 3*(x**2) + 6*x + 7
h = lambda x: x + 2

x = np.linspace(-1,1)
y = h(x)

plt.figure(1)
plt.plot(x, P(x), label = 'P(x)')
plt.plot(x, h(x), label = 'h(x)')
plt.title('Funciones P(x) y h(x)')
plt.xlabel('x')
plt.legend()
plt.show()

n = len(x)

z = np.zeros(2*n-1)

for i in range(1,2*n):
    z[i-1] = np.multiply(P(x), nt.shift(h(-x),-n+i)).sum()

plt.figure(2)
plt.plot(z)
plt.title('Resultado convolución entre P(x) y h(x)')
plt.xlabel('x')
plt.ylabel('z(x)')
plt.legend()
plt.show()

# Observación: error en la escala de tiempo del resultado (corregir).

#%% Ejercicio 2: Filtrado (detección de bordes) de la imagen Lenna.png 
#                utilizando el kernel sobel y convolución en dos dimensiones.

import numpy as np
import pylab as pl

path = 'C:\\Users\\Administrador\\Pictures\\Lenna.png'

src = pl.imread(path)

pl.figure(1)
pl.imshow(src, cmap = pl.cm.gray)

src = np.matrix(src[:,:,2],'float')

pl.figure(2)
pl.imshow(src, cmap = pl.cm.gray)

m = np.size(src, axis = 0)
n = np.size(src, axis = 1)

KernelH = np.matrix([[-1,-2,-1],[0,0,0],[1,2,1]],'float')
KernelV = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]],'float')

stackColumns = np.ones((n,1))
src = np.hstack((stackColumns, src, stackColumns))
stackRows = np.ones((1,m + 2))
src = np.vstack((stackRows, src, stackRows))

dstH = np.ones_like(src)
dstV = np.ones_like(src)

for i in range(1,m):
    for j in range(1,n):
        dstH[i,j] = np.multiply(src[i-1:i+2,j-1:j+2],KernelH).sum()

for i in range(1,m):
    for j in range(1,n):
        dstV[i,j] = np.multiply(src[i-1:i+2,j-1:j+2],KernelV).sum()

dst = np.sqrt(np.power(dstH[1:m+1,1:n+1],2) + np.power(dstV[1:m+1,1:n+1],2))

pl.figure(3)
pl.imshow(dst, cmap = pl.cm.gray)

# Observación: se debe colocar la ruta de la imagen "Lena.png" en "path".

#%% Ejercicio 3: Eigenvalor dominante (1er valor propio) de una matriz.

from numpy import linalg as lng
import numpy as np

def maxEigValue(A, x0, tol):
    x = A*x0
    d = np.max(np.abs(x))
    x = np.divide(x, d)
    
    while (lng.norm(x - x0) > tol):
        x0 = x
        x = A*x0
        d = np.max(np.abs(x))
        x = np.divide(x, d)
    
    d = np.round(d, 2)
    x = np.round(x, 2)
    
    return d, x


D = np.matrix([[1,-3,8],[2,-5,9],[3,-6,10]], 'float')

x0 = np.ones((3,1))
tol = 1e-3

d, x, = maxEigValue(D, x0, tol)

X = lng.eig(D)
np.round(np.real(np.max(X[0])),2)

print(f"El valor propio d = {d}, coincide con el calculado por " +
      f"eig(D) = {np.round(np.real(np.max(X[0])),2)}.")

# Observación: en lugar de indicar el número de iteraciones, estas son
#              definidas por el programa de acuerdo a la comparación entre la
#              tolerancia y la aproximación (diferencia) entre el valor
#              calculado para x y el de la iteración anterior.
#              Esto se hace para evitar gastar ciclos innecesariamente cuando
#              se busca un decimal de precisión en el resultado.