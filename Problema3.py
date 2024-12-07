# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 3: Flujo alrededor de una cepa de un puente
# ================================================================

# Este código grafica las líneas de corriente y el campo de velocidades alrededor de la cepa de un puente.
# La función de corriente se define como ψ = U * r * (1 - (a^2 / r^2)) * sin(θ), con r y θ en coordenadas polares.

# Parámetros del problema
a = 5  # Radio de la cepa del puente [m]
U = 1  # Velocidad uniforme lejos de la cepa [m/s]

# Definimos el dominio en coordenadas cartesianas
x = np.linspace(-15, 15, 400)  # Rango de valores de x
y = np.linspace(-15, 15, 400)  # Rango de valores de y
X, Y = np.meshgrid(x, y)  # Generamos una malla de puntos en el plano xy

# Conversión de coordenadas cartesianas a polares
R = np.sqrt(X**2 + Y**2)  # Distancia radial desde el origen
Theta = np.arctan2(Y, X)  # Ángulo polar desde el eje x
R[R == 0] = 1e-10  # Se evita división por cero al calcular 1 / R

# Calculamos la función de corriente ψ
# ψ representa las líneas de corriente del flujo ideal alrededor de la cepa
psi = U * R * (1 - (a**2 / R**2)) * np.sin(Theta)

# Cálculo de las derivadas de ψ en coordenadas polares
# Estas derivadas se usan para obtener las componentes de la velocidad
dpsi_dtheta = U * R * (1 - (a**2 / R**2)) * np.cos(Theta)  # ∂ψ/∂θ
dpsi_dr = (U * (1 - (a**2 / R**2)) * np.sin(Theta) +
           U * R * (2 * a**2 / R**3) * np.sin(Theta))  # ∂ψ/∂r

# Cálculo de las componentes de velocidad en coordenadas polares
v_r = (1 / R) * dpsi_dtheta  # Velocidad radial
v_theta = -dpsi_dr  # Velocidad angular

# Transformamos las velocidades a coordenadas cartesianas
U_cart = v_r * np.cos(Theta) - v_theta * np.sin(Theta)  # Componente x de la velocidad
V_cart = v_r * np.sin(Theta) + v_theta * np.cos(Theta)  # Componente y de la velocidad

# Máscara para excluir el interior de la cepa (R < a)
mask = R < a  # Identificamos puntos dentro de la cepa
U_cart[mask] = np.nan  # Asignamos valores nulos para evitar cálculo en la cepa
V_cart[mask] = np.nan

# Calculamos la magnitud de la velocidad para fines visuales
speed = np.sqrt(U_cart**2 + V_cart**2)

# Graficamos las líneas de corriente
plt.figure(figsize=(8, 6))
contours = plt.contour(X, Y, psi, levels=50, cmap='viridis')  # Contornos de ψ con 50 niveles
circle = plt.Circle((0, 0), a, color='black', fill=False, linewidth=2)  # Representación de la cepa
plt.gca().add_patch(circle)  # Añadimos la cepa al gráfico
plt.title('Líneas de corriente alrededor de la cepa de un puente')  # Título del gráfico
plt.xlabel('x [m]')  # Etiqueta del eje x
plt.ylabel('y [m]')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.colorbar(contours, label='Función de corriente ψ')  # Barra de color para ψ
plt.show()

# Graficamos el campo de velocidades con magnitud
plt.figure(figsize=(8, 6))
plt.streamplot(
    X, Y, U_cart, V_cart, color=speed, cmap='cool', density=2  # Líneas de flujo coloreadas por magnitud
)
circle = plt.Circle((0, 0), a, color='black', fill=True)  # Representación de la cepa como un círculo sólido
plt.gca().add_patch(circle)  # Añadimos la cepa al gráfico
plt.title('Campo de velocidades alrededor de la cepa de un puente (con magnitud)')  # Título del gráfico
plt.xlabel('x [m]')  # Etiqueta del eje x
plt.ylabel('y [m]')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.colorbar(label='Magnitud de velocidad [m/s]')  # Barra de color para la magnitud de velocidad
plt.show()
