import numpy as np
def testen(L,A):
 LT = np.transpose(A)
 if(np.dot(L , LT) = A):
     print("Test hat funktioniert")
    else:
     print("Fehler, Ausgabe ist nicht korrekt")