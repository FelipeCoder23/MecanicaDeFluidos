# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 2: Campo de velocidades en una esquina de 90 grados
# ================================================================

# Explicación:
# Graficaremos el campo de velocidades y las líneas de corriente para un flujo cerca de una esquina de 90°.
# La función de corriente es ψ = 2 * r^2 * sin(2θ)

# Definimos el dominio en coordenadas polares
r = np.linspace(0, 1, 200)
theta = np.linspace(0, np.pi/2, 200)
R, Theta = np.meshgrid(r, theta)

# Convertimos a coordenadas cartesianas para graficar
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Calculamos la función de corriente ψ
psi = 2 * R**2 * np.sin(2 * Theta)

# Calculamos las componentes del campo de velocidades en coordenadas polares
# v_r = (1/r) ∂ψ/∂θ
# v_θ = -∂ψ/∂r
v_r = (1 / R) * 4 * R**2 * np.cos(2 * Theta)
v_theta = -4 * R * np.sin(2 * Theta)

# Convertimos las velocidades a coordenadas cartesianas
U = v_r * np.cos(Theta) - v_theta * np.sin(Theta)
V = v_r * np.sin(Theta) + v_theta * np.cos(Theta)

# Graficamos las líneas de corriente
plt.figure(figsize=(8, 6))
plt.contour(X, Y, psi, levels=50, cmap='viridis')
plt.title('Líneas de corriente cerca de una esquina de 90°')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.colorbar(label='Función de corriente ψ')
plt.show()

# Graficamos el campo de velocidades
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V)
plt.title('Campo de velocidades cerca de una esquina de 90°')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()
