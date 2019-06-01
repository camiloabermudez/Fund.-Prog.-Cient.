#%% Ejercicio 1: minimizar la función f(x) = x1 * x4 * (x1 + x2 + x3) + x3
#                sujeto a:
#
#                Restricciones:   x1 * x2 * x3 * x4 >= 25
#                                 x1**2 + x2**2 + x3**2 + x4**2 = 40
#                Rango:           1 <= x1, x2, x3, x4 <= 5
#                Semilla:         x0 = (1, 5, 5, 1)

from scipy.optimize import minimize

def objective(x):
    x1, x2, x3, x4 = x
    return x1 * x4 * (x1 + x2 + x3) + x3

def constraint_1(x):
    x1, x2, x3, x4 = x
    return x1 * x2 * x3 * x4 - 25.0

def constraint_2(x):
    x1, x2, x3, x4 = x
    return 40 - (x1**2 + x2**2 + x3**2 + x4**2)

constrts = [{'type':'ineq', 'fun':constraint_1},
            {'type':'eq',   'fun':constraint_2}]

b = (1.0, 5.0)
bnds = (b, b, b, b)

x0 = [1, 5, 5, 1]

sltn = minimize(objective, x0, method = 'SLSQP', \
                bounds = bnds, constraints = constrts)

print(f"El valor mínimo de la función es f(x) = {sltn.fun}.\n" +
      f"El argumento que la minimiza es: x = {sltn.x}")

#%% Ejercicio 2: resuelva con "minimize":
#                min f(x) = -2 * x1 * x2 + 2 * x1 - x1**2 - 2 * x2**2
#                sujeto a:
#
#                Restricciones:     x1**3 - x2 = 0
#                                   x2 - (x1 - 1)**4 - 2 >= 0
#                Rango:             0.5 <= x1 <= 1.5; 1.5 <= x2 <= 2.5
#                Semilla:           x0 = (0, 2.5)

from scipy.optimize import minimize

def objective(x):
    x1, x2 = x
    return -2 * x1 * x2 + 2 * x1 - x1**2 - 2 * x2**2

def constraint_1(x):
    x1, x2 = x
    return x1**3 - x2

def constraint_2(x):
    x1, x2 = x
    return x2 - (x1 - 1)**4 - 2

constrts = [{'type':'eq',   'fun':constraint_1},
            {'type':'ineq', 'fun':constraint_2}]

b1 = (0.5, 1.5)
b2 = (1.5, 2.5)
bnds = (b1, b2)

x0 = [0, 2.5]

sltn = minimize(objective, x0, method = 'SLSQP', \
                bounds = bnds, constraints = constrts)

print(f"El valor mínimo de la función es f(x) = {sltn.fun}.\n" +
      f"El argumento que la minimiza es: x = {sltn.x}")

#%% Ejercicio 3: resuelva con "linprog":
#                max f(x, y) = x + y
#                sujeto a:
#
#                Restricciones:     50 * x + 24 * y <= 2400
#                                   30 * x + 33 * y <= 2100
#                Rango:             x, y >= 0

from scipy.optimize import linprog

# la función "linprog" siempre miniza la función objetivo.
# Para maximizarla, se hace max(f(x)) == -min(-f(x)).

c = [-1, -1]
A = [[50, 24], [30, 33]]
b = [2400, 2100]
bnds = (0, None)

sltn = linprog(c, A, b, bounds = bnds, method = 'simplex')

print(f"El valor máximo de la función es f(x) = {(-1)*sltn.fun}.\n" +
      f"El argumento que la maximiza es: x = {sltn.x}")

#%% Ejercicio 4: Maximizar el retorno de venta (ingreso, utilidad):
#                max f(pt, xt) = sum(pt * xt)
#                sujeto a:
#
#                Restricciones:     xt <= s0
#                Rango:             0 <= xt <= A/B



