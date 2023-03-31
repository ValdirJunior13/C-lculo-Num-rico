import numpy as np
import math
import time

def norma_inf(u,v):
  n = len(u)
  d = 0
  for i in range(0, n):
    d_max = abs(u[i] - v[i])
    if(d_max > d):
      d = d_max
  return d
  
#gauss jacobi
def gauss_jacobi(a,b, max_k: int, e):
  n = len(b)
  #condição inicial
  x_anterior = n*[1]
  #vetor solução 
  x_atual = n*[0]
  for k in range(1, max_k + 1):
    #atualiza o vetor solução
    for i in range(0, n):
      s = 0
      for j in range(0,n):#percorre as colunas
        if(j != i): #coluna j diferente da linha i
          s +=  a[i][j]*x_anterior[j]
         
      x_atual[i] = (b[i] - s)/a[i][i]
    t = norma_inf(x_atual, x_anterior)
    if (t < e):
      break
    else: 
      x_anterior = x_atual[:]
      
  return k, x_atual
       


a = [[0, -4, -10], [0,69, 65], [0, -65, 80]]
v = [64, 144, 10]
e = 0.001


k_iteracoes, x_sol = gauss_jacobi(a, v, 10, e)
print("número de iterações foi {} e o resultado foi: {}" .format(k_iteracoes, x_sol))


      
