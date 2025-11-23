import numpy as np
import matplotlib.pyplot as plt

def divDiff(x, f):
    
    """
    Berechnet die dividierten Differenzen für gegebene Stuetzstellen x und Funktionswerte f.
    Gibt die Koeffizienten des Newton-Polynoms zurück.
    """
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = f

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (x[i+j] - x[i])
    
    return F[0, :]   

def hornerSchema(t, a, x):
    """
    Wertet Newton-Polynom mit Koeffizienten a und Stuetzstellen x an Punkten t aus.
    t kann ein Skalar oder NumPy-Array sein.
    """
    t = np.array(t, dtype=float)
    n = len(a)
    p = np.zeros_like(t)

    for k in range(n-1, -1, -1):
        p = a[k] + (t - x[k]) * p

    return p


x = np.arange(-5, 6)             
f = 1 / (1 + x**2)               


a = divDiff(x, f)


t = np.linspace(-6, 6, 500)
p = hornerSchema(t, a, x)

# Plot
plt.figure(figsize=(8,5))
plt.plot(t, p, label="Interpolation", linewidth=2)
plt.scatter(x, f, color="red", label="Stuetzstellen")
plt.title("Newton-Interpolation von f(x)=1/(1+x²)")
plt.legend()
plt.grid(True)
plt.show()
