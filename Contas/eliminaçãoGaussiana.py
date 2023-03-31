#elminação gaussiana
 #A = matriz dos coeficientes, b é o vetor dos termos independentes
import numpy
def gauss(A, b):
  n = len(b) #tamanho de b
  for k in range(0, n-1):
    pivo = a[k][k] #selecionar o pivo
  

for i in range(k+1, n):
  multiplicador = A[i][k]/pivo
  for j in range:
    A[i][j] = A[i][j] - multiplicador*A[k][j]
    b[i] = b[i] - multiplicador * b[k]



A = [[3,2,4], [1,1,2],[4,3,-2]]
b = [1,2,3]

A_t, b_t = gauss(A,b)
print(A_t)
print(b_t)