import numpy
def subs_reversa(A,b):
  n = len(b)
  x = n*[0]

x[n-1] = b[n-1]/A[n-1][n-1]

for k in range(n-2, -1, -1):
  s = 0
  for j in range(k+1,n):
    s = s + A[k][j]*x[j]
    x[k] = (b[k] - s)/A[k][k]
x = subs_reversa(A, b)