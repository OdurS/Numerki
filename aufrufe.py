import Gauss_Jordan as gj
import manuelle_eingabe as me
import numpy as np
def manual_auswahl():
    """führt den Gauß_JOrdenbefehl aus für eine Matrix, die man eingeben kann
    """
    A = me.Matix_eingabe()
    gj.Gauss_Jordan(A)
    
def Beispiel_1(): 
    """führt den Gauß_JOrdenbefehl aus für die  Matrix A1
    """
    A1= [
    [4,  2,  8,  1,  3],
    [-2, 2,  5, -6,  9],
    [7, -1,  2,  4,  5],
    [5,  3,  7, -2,  2],
    [3,  5,  8, -3,  1]
                        ]
    gj.Gauss_Jordan(A1)
    print("-------------------------------")
    print("A1_invers ohne rundungsfehler:\n"  + str(np.linalg.inv(A1)))
    
def Beispiel_2():
    """führt den Gauß_JOrdenbefehl aus für die  Matrix A1
    """ 
    A2 = [
    [4, -2,  0,  1,  3],
    [-2, 5,  0, -6,  9],
    [0,  0,  0,  4,  5],
    [5, -3,  7, -4,  2],
    [3,  5,  8, -3,  1]
                         ] 
    gj.Gauss_Jordan(A2)
    print("-------------------------------")
    print("A1_invers ohne rundungsfehler:\n" + str(np.linalg.inv(A2)))