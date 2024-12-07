# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 2: Campo de velocidades en una esquina de 90 grados
# ================================================================

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
v_r = (1 / R) * 4 * R**2 * np.cos(2 * Theta)
v_theta = -4 * R * np.sin(2 * Theta)

# Evitamos posibles problemas de indefinición en r=0
v_r[R == 0] = 0
v_theta[R == 0] = 0

# Convertimos las velocidades a coordenadas cartesianas
U = v_r * np.cos(Theta) - v_theta * np.sin(Theta)
V = v_r * np.sin(Theta) + v_theta * np.cos(Theta)

# Calculamos la magnitud de la velocidad
speed = np.sqrt(U**2 + V**2)

# Graficamos las líneas de corriente
plt.figure(figsize=(8, 6))
plt.contour(X, Y, psi, levels=50, cmap='viridis')
plt.title('Líneas de corriente cerca de una esquina de 90°')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.colorbar(label='Función de corriente ψ')
plt.show()

# Graficamos el campo de velocidades con densidad reducida y escala de colores
plt.figure(figsize=(8, 6))
plt.quiver(X[::5, ::5], Y[::5, ::5], U[::5, ::5], V[::5, ::5], speed[::5, ::5], cmap='cool')
plt.title('Campo de velocidades cerca de una esquina de 90° (con magnitud)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.colorbar(label='Magnitud de velocidad')
plt.show()
