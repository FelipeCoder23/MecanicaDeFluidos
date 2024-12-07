# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 3: Flujo alrededor de una cepa de un puente
# ================================================================

# Explicación:
# Representaremos el flujo ideal alrededor de la cepa de un puente usando la función de corriente dada:
# ψ = U * r * (1 - (a^2 / r^2)) * sin(θ)

# Parámetros
a = 5    # Radio de la cepa del puente
U = 1    # Velocidad del flujo en m/s

# Dominio
x = np.linspace(-15, 15, 400)
y = np.linspace(-15, 15, 400)
X, Y = np.meshgrid(x, y)

# Conversión a polares
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)
R[R == 0] = 1e-10

# Función de corriente
psi = U * R * (1 - (a**2 / R**2)) * np.sin(Theta)

# Cálculo de derivadas
dpsi_dtheta = U * R * (1 - (a**2 / R**2)) * np.cos(Theta)
dpsi_dr = U * (1 - (a**2 / R**2)) * np.sin(Theta) + U * R * (2 * a**2 / R**3) * np.sin(Theta)

# Velocidades en polares
v_r = (1 / R) * dpsi_dtheta
v_theta = -dpsi_dr

# Transformación a Cartesianas
U_cart = v_r * np.cos(Theta) - v_theta * np.sin(Theta)
V_cart = v_r * np.sin(Theta) + v_theta * np.cos(Theta)

# Máscara para interior de la cepa: R < a
mask = R < a
U_cart[mask] = np.nan
V_cart[mask] = np.nan

# Gráfica de líneas de corriente
plt.figure(figsize=(8, 6))
contours = plt.contour(X, Y, psi, levels=50, cmap='viridis')
circle = plt.Circle((0, 0), a, color='black', fill=False, linewidth=2)
plt.gca().add_patch(circle)
plt.title('Líneas de corriente alrededor de la cepa de un puente')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.axis('equal')
plt.colorbar(contours, label='Función de corriente ψ')
plt.show()

# Gráfica del campo de velocidades con streamplot
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, U_cart, V_cart, density=2, color='blue')
circle = plt.Circle((0, 0), a, color='black', fill=True)
plt.gca().add_patch(circle)
plt.title('Campo de velocidades alrededor de la cepa de un puente')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.axis('equal')
plt.show()