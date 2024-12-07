# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 1: Vórtice
# ================================================================

# Explicación:
# Vamos a graficar las líneas de corriente, el campo de velocidades y la función potencial para un vórtice.
# La función de corriente dada es ψ = ln(x^2 + y^2)

# Definimos el dominio
x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)

# Calculamos la función de corriente ψ
psi = np.log(X**2 + Y**2)

# Calculamos el potencial φ (función potencial)
# Para un vórtice, el potencial φ = arctan2(y, x)
phi = np.arctan2(Y, X)

# Calculamos las componentes del campo de velocidades
# Para un vórtice:
# v_x = -∂ψ/∂y
# v_y = ∂ψ/∂x
U = -2 * Y / (X**2 + Y**2)
V = 2 * X / (X**2 + Y**2)

# Graficamos las líneas de corriente
plt.figure(figsize=(8, 6))
plt.contour(X, Y, psi, levels=50, cmap='viridis')
plt.title('Líneas de corriente de un vórtice')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.colorbar(label='Función de corriente ψ')
plt.show()

# Graficamos el campo de velocidades
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, U, V, density=2, color='blue')
plt.title('Campo de velocidades de un vórtice')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()

# Graficamos la función potencial
plt.figure(figsize=(8, 6))
plt.contour(X, Y, phi, levels=50, cmap='plasma')
plt.title('Función potencial φ de un vórtice')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.colorbar(label='Función potencial φ')
plt.show()