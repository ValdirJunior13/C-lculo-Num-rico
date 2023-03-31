#método do ponto fixo

import math
import time

def f(x):
  return x**3 + x**2 - x + 1
def phi(x):
  return math.sqrt(-x**2 + x - 1)
a = 0.5
e = 0.00001
k = 0

x = a
while abs(f(x)) > e:
  x = phi(x)
  print(x)
 
  k = k + 1
 
print("A raiz encontrada foi: ", x)
print("O número de iterações foi: ", k)

