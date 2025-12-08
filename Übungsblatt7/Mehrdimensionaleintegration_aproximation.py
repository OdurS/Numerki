import numpy as np
import sympy as sp

def f(x, y):
    """Zu integrierende Funktion f(x,y)"""
    return x**2 * y - x * y**2 + 3

def simpson_1d_weights(n):
    """Erzeugt die Simpson-Gewichte für n Unterintervalle (n muss gerade sein)"""
    if n % 2 != 0:
        raise ValueError("n muss gerade sein")
    w = np.ones(n+1)
    for i in range(1, n):
        w[i] = 4 if i % 2 == 1 else 2
    return w

def simpson_2d(f, ax, bx, ay, by, nx=20, ny=20):
    """Berechnet das 2D-Simpson-Integral  auf [ax,bx] × [ay,by] mittels Tensorprodukt"""
    if nx % 2 or ny % 2:
        raise ValueError("nx und ny müssen gerade  sein")
    x = np.linspace(ax, bx, nx+1)
    y = np.linspace(ay, by, ny+1)
    hx = (bx - ax) / nx
    hy = (by - ay) / ny
    wx = simpson_1d_weights(nx)
    wy = simpson_1d_weights(ny)
    X, Y = np.meshgrid(x, y, indexing="ij")
    F = f(X, Y)
    return (hx/3) * (hy/3) * np.sum(wx[:,None] * wy[None,:] * F)

def exact_rect(a, b, c, d):
    """Berechnet das exakte Integral von f(x,y) über [a,b] × [c,d]"""
    x, y = sp.symbols('x y')
    integral_y = sp.integrate(f(x, y), (y, c, d))
    integral_xy = sp.integrate(integral_y, (x, a, b)) #Ich hab integral von  sympy benutzt
    return float(integral_xy)

I_Ganz  = simpson_2d(f, 0, 6, 0, 6, nx=40, ny=40)
I_fehlend = simpson_2d(f, 2, 4, 2, 4, nx=40, ny=40)
I_a = I_Ganz - I_fehlend

I_b = 0.0
for i in range(1, 4):
    for j in range(1, 4):
        if (i, j) == (2, 2):
            continue
        ax = 2*(i-1)
        bx = 2*i
        ay = 2*(j-1)
        by = 2*j
        I_b += simpson_2d(f, ax, bx, ay, by, nx=20, ny=20)

I_exact = exact_rect(0, 6, 0, 6) - exact_rect(2, 4, 2, 4)

print("Approximation (a):", I_a)
print("Approximation (b):", I_b)
print("Exakter Wert:", I_exact)
