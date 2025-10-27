import numpy as np
def Gauss_Jordan(A):
 reihen = len(A)
 Spalten = len(A[0])
 if(reihen != Spalten):
     raise ValueError("keine invertierbare Matrix")
 n = reihen
 det = np.linalg.det(A) 
 if(det != 0):
     raise ValueError("keine invertierbare Matrix")
 
 
 I = np.zeros((n, n))
 A_ZSF, I_ZSF =Zeilenstufenform(A,I)
 
 for i in range(n-1, -1, -1): 
        pivot = A_ZSF[i][i]
        if abs(pivot) < 1e-12:
            continue  
        for j in range(n):
            A_ZSF[i][j] /= pivot
            I_ZSF[i][j] /= pivot
        for k in range(i):
            faktor = A_ZSF[k][i]
            for j in range(n):
                A_ZSF[k][j] -= faktor * A_ZSF[i][j]
                I_ZSF[k][j] -= faktor * I_ZSF[i][j] 
 
 
 
def Zeilenstufenform(A;I):
    """Formt A in ZSF um ein führt die selben umformungen auf I durch

    Args:
        A (Matix): umzuformende matrix

    Returns:
        Matix: A in Zeilenstufenform, Selbe umformungen auf I angewendet
    """
    n = len(A)
    A = [row[:] for row in A]
    reihe = 0
    
    for spalte in range(n):
        pivot_row = max(range(reihe, n), key=lambda i: abs(A[i][spalte]))
        if abs(A[pivot_row][spalte]) < 1e-12:
            continue  

        A[reihe], A[pivot_row] = A[pivot_row], A[reihe]
        I[reihe], I[pivot_row] = I[pivot_row], I[reihe]

        for i in range(reihe+1, n):
            factor = A[i][spalte] / A[reihe][spalte]
            for j in range(spalte, n):
                A[i][j] -= factor * A[reihe][j]
            for j in range(n):
                I[i][j] -= factor * I[reihe][j]

        reihe += 1

    return A, I

