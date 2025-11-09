import numpy as np
def Cholesky(A):
 reihen = len(A)
 Spalten = len(A[0])
 if(reihen != Spalten):
     raise ValueError("keine nxn-Matrix")
 if not np.array_equal(A, np.transpose(A)):
     raise ValueError("Matrix nicht symmetrisch")
 if(np.all(np.linalg.eigvals(A) <= 0)):
     raise ValueError("Matrix ist nicht positiv definit")
 L = np.zeros((reihen, reihen))
 L[0][0] = (A[0][0])**0.5
 n = reihen
 for i in range(1, n):
     for j in range(0, i):
        summe1 = 0
        for k in range(0, j):       
         summe1 += L[i][k] * L[j][k]
        L[i][j] = (1/(L[j][j]))*((A[i][j]) - summe1)
     summe2 = 0
     for p in range(0, i):       
         summe2 += (L[i][p])**2 
     L[i][i] = ((A[i][i]) - summe2 )**0.5 
 return L
        