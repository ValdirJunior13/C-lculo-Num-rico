#método da bissecção 
import math 
def f(x):
  return math.pow(x,3) + math.pow(x,2) - x + 1 

k = 0  #iterações iniciais em 0
a = -2 
b = -1
e = 0.00001 #precisão 

if f((a+b)/2) < e: 
  print("A raiz encontrada foi: ", (a+b)/2)
  
else: 
  while b - a > e: 
    m = (a + b)/2
    if f(a)*f(m) < 0:
      b = m
    else:
      a = m
    k = k + 1
  print("A raiz encontrada foi: ", m)
  print("O número de iterações foi: ", k)  


