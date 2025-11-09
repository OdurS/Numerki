import manuelle_eingabe as me
import Cholesky as ch
import test as t
def Beispiel():
    A=[
    [16, 4,  4,  0],
    [4,  5,  1,  2],
    [4,  1,  2, -1],
    [0,  2, -1,  6],
    ]
    
    L = ch.Cholesky(A)
    print("-------------------------------")
    print(L)
    print("-------------------------------")
    t.testen(L,A)
    
def manual_auswahl():
    A = me.Matix_eingabe()
    L = ch.Cholesky(A)
    print("-------------------------------")
    print(L)
    print("-------------------------------")
    t.testen(L,A)