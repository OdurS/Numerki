import numpy as np
def testen(L,A):
 LT = np.transpose(L)
 if(np.array_equal(np.dot(L,LT) , A)):
     print("Test hat funktioniert")
 else:
     print("Fehler, Ausgabe ist nicht korrekt")