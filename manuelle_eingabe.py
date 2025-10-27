def Matix_eingabe():
    """eine Manuelle Eingabe einer Matrix, durch Zeilenweises eintragen der Zahlen

    Raises:
        ValueError: es wurden mehr als n viele Zahlen pro Zeile eingegeben
    """
    
    n = int(input("Dimension n eingeben: "))
    A = []

    print("Bitte die Matrixzeilen eingeben (jeweils durch Leerzeichen getrennt):")
    for i in range(n):
        row = list(map(float, input(f"Zeile {i+1}: ").split()))
        if len(row) != n:
            raise ValueError("Falsche Anzahl von Elementen!")
        A.append(row)