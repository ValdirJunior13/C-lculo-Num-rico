import numpy as np
import math

def eliminacao_Gaussiana(A,b):
    n = len(b)
  
    for k in range(0,n-1):
         for i in range(k+1,n):
            m = A[i][k] / A[k][k]  #multiplicador baseando no pivo escolhido
            for j in range(k,n):
                A[i][j] -= A[k][j] * m  # novos valores para a linha i da matriz 
            b[i]-= b[k] * m   # novo valores par os termos independentes
 
    return A,b

def substituicao_reversa(A,b): # algoritmo para encontrar o vetor solução
    n = len(b)
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1][n-1] # soluçao inicial para para a matriz de hilbert considerando Ax = b, temos  x = b/A 

    for k in range(n-1,0,-1):
        s = 0    
        for j in range(k+1,n):
            s += A[k-1][j-1] * x[j-1]  # multiplica o valor da solução anterior para termos apenas uma incognita
        x[k-1] = (b[k-1] - s) / A[k-1][k-1] # descobre uma nova solução
    return x 


def matriz_de_vandermonde(matriz,n):
    for i in range(0,n):
        for j in range(0,n):
            matriz[i][j] = math.pow(temperatura[i],j)
          
def equacao_polinomial(vetor_solucao,x):
    polinomio = 0
    for i in range(0,len(vetor_solucao)-1):
        polinomio += vetor_solucao[i] * math.pow(x,i)
    return polinomio    

def equacao_polinomial_2(vetor_solucao,x):
    polinomio = 0
    for i in range(0,len(vetor_solucao)-1):
        polinomio += vetor_solucao[i] * math.pow(x,i)
    return polinomio - 0.99837 


#dados iniciais
temperatura = [30,35,40]
calor_especifico = [0.99826 ,0.99818 ,0.99828]

#tamanho do sistema
n = len(temperatura)
matriz = np.zeros((n,n)) #matriz dos coeficientes

matriz_de_vandermonde(matriz,n) #preparação para matriz de Vandermon
eliminacao_Gaussiana(matriz,calor_especifico) # os resultados ja são alterados dentro da variavel  matriz
vetor_solucao = substituicao_reversa(matriz,calor_especifico) # resolve o sistema por substituição reversa

print("Os coeficientes dos polinomios são: \n")
for j in range(0,n):
    print("a[",j,"] =",vetor_solucao[j])

print("\nO valor para o calor específico da água no polinimo de grau 2 é:\n p(32.5) =",equacao_polinomial(vetor_solucao,32.5))


# dados iniciais 
temperatura = [20,25,30,35,40,45,50]
calor_especifico = [0.99907, 0.99852, 0.99826 ,0.99818 ,0.99828, 0.99849, 0.99878]



#tamanho do sistema
n = len(temperatura)
matriz = np.zeros((n,n)) #matriz dos coeficientes


matriz_de_vandermonde(matriz,n) #preparação para matriz de Vandermon
eliminacao_Gaussiana(matriz,calor_especifico) # os resultados ja são alterados dentro da variavel  matriz
vetor_solucao = substituicao_reversa(matriz,calor_especifico) # resolve o sistema por substituição reversa

print("Os coeficientes dos polinomios são: \n")
for j in range(0,n):
    print("a[",j,"] =",vetor_solucao[j])

print("\nO valor para o calor específico da água no polinimo de grau 6 é:\n p(32.5) =",equacao_polinomial(vetor_solucao,32.5))


a = 40
b = 45
erro = 0.00001

while b-a > erro :
    m = (a+b)/2
    if equacao_polinomial_2(vetor_solucao,a) * equacao_polinomial_2(vetor_solucao,m) < 0:
        b = m
    else:
        a = m

print("A temperatura para o calor especifico, onde o polinomio de grau 6 é p(x) = 0.99837 da função é:",m)