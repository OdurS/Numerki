import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

A = imread("Übungsblatt9\cameraman.jpg")

m, n = A.shape
min_mn = min(m, n)

U, S, Vt = np.linalg.svd(A, full_matrices=False)  # A = U S V^T

rel_errors = []

for k in range(min_mn + 1):
    S_k = np.zeros_like(S)
    S_k[:k] = S[:k]
    A_k = (U * S_k) @ Vt
    rel_error = np.linalg.norm(A - A_k, 'fro') / np.linalg.norm(A, 'fro')
    rel_errors.append(rel_error)

plt.figure(figsize=(6,4))
plt.plot(range(min_mn + 1), rel_errors, marker='o')
plt.xlabel("Approximationsrang k")
plt.ylabel("Relativer Fehler ||A - A_k||_F / ||A||_F")
plt.title("SVD-Approximation: Relativer Fehler vs Rang k")
plt.grid(True)
plt.show()


error_levels = [0.10, 0.05, 0.01, 0.001]  
approx_images = []

for tol in error_levels:
    k = next(i for i, err in enumerate(rel_errors) if err <= tol)
    S_k = np.zeros_like(S)
    S_k[:k] = S[:k]
    A_k = (U * S_k) @ Vt
    approx_images.append((k, A_k))

fig, axes = plt.subplots(1, 4, figsize=(16,4))
for ax, (k, img), tol in zip(axes, approx_images, error_levels):
    ax.imshow(img, cmap='gray')
    ax.set_title(f"k={k}, Fehler<{tol*100:.1f}%")
    ax.axis('off')
plt.show()




print(f"Originalbild: {m} x {n} = {m*n} Einträge")
for k, _ in approx_images:
    storage = k*(m+n+1)
    print(f"Rang {k}: Speicheraufwand = {storage} Einträge (Uk + Σk + Vk)")