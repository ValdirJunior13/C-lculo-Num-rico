
# ajusta o conjunto de dados à uma curva suave pre-definida
# resolve o sistema linear G*alphas = b em que G[i][j] = <g_i,g_j> e b_i = <y,g_i>
# onde g_i, i=1,2,...,n são as funções pré-definidas calculadas nos pontos x_k
# do conjunto de dados e x, y são os vetores do conjunto de dados
import math
import numpy as np
from matplotlib import pyplot as plt
def gauss(p, w):
    n = len(w)
    # lecionando o pivô  (elemento da diagonal)
    for k in range(0, n - 1):
        # para cada linha abaixo do pivô
        for i in range(k + 1, n):
            m = p[i][k] / p[k][k]
            # para cada coluna na linha i atualizamos os termos
            for j in range(k, n):
                p[i][j] = p[i][j] - m * p[k][j]
            w[i] = w[i] - m * w[k]

    return p, w
def subs(a, r):
    n = len(r)
    x = n * [0]

    x[n - 1] = r[n - 1] / a[n - 1][n - 1]

    # para cada linha acima da última solução
    for k in range(n - 1, -1, -1):
        s = 0
        # para cada coluna na linha k
        for j in range(k + 1, n):
            s = s + a[k][j] * x[j]
        x[k] = (r[k] - s) / a[k][k]

    return x
# define as funções
def g_1(u):
    return 1

def g_2(r):
    return r

def g_3(p):
    return math.exp(p)


dados = np.loadtxt("dados.txt", float)
x = dados[:, 0]
y = dados[:, 1]

# determina a matriz G
# dimensão do sistema (número de funções g_i)
n = 3
G = np.zeros((n, n))
b = n * [0]
# número de pontos no conjunto de dados
m = len(x)
G_aux = np.zeros((m, n))

for k in range(0, m):
    G_aux[k, 0] = g_1(x[k])
    G_aux[k, 1] = g_2(x[k])
    G_aux[k, 2] = g_3(x[k])

for i in range(0, n):
    for j in range(0, n):
        G[i][j] = sum(G_aux[:, i] * G_aux[:, j])
    b[i] = sum(y[:] * G_aux[:, i])

# Resolve o sistema linear para determinar os coeficientes "alphas"
A_t, b_t = gauss(G, b)
alphas = subs(A_t, b_t)

print(20 * "--")
print("coeficientes = ", alphas)


def phi(p):
    return alphas[0] * g_1(p) + alphas[1] * g_2(p) + alphas[2] * g_3(p)


# Erro
r_s = 0
for k in range(0, m):
    r_s = r_s + math.pow(phi(x[k]) - y[k], 2)
r_s = math.sqrt(r_s)

print(20 * "--")
print("Erro geral quadrático =", r_s)
print(20 * "--")

# cria conjunto de dados para plotagem da curva de ajuste
x_phi = np.arange(min(x), max(x), 0.01).tolist()
phi_plot = len(x_phi) * [0]
for i in range(0, len(phi_plot)):
    phi_plot[i] = phi(x_phi[i])

plt.plot(x, y, 'o')
plt.plot(x_phi, phi_plot, 'r--', label='$\phi(x)$')
plt.legend()
plt.show()