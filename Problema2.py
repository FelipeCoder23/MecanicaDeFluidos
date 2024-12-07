# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 2: Campo de velocidades en una esquina de 90 grados
# ================================================================

# Este código grafica las líneas de corriente y el campo de velocidades cerca de una esquina de 90°.
# La función de corriente se define como ψ = 2r^2 sin(2θ), donde r y θ son coordenadas polares.

# Definimos el dominio en coordenadas polares
r = np.linspace(0, 1, 200)  # Valores radiales desde 0 hasta 1
theta = np.linspace(0, np.pi/2, 200)  # Valores angulares desde 0 hasta π/2 (90°)
R, Theta = np.meshgrid(r, theta)  # Generamos una malla en coordenadas polares

# Convertimos a coordenadas cartesianas para facilitar los gráficos
X = R * np.cos(Theta)  # Componente x de las coordenadas cartesianas
Y = R * np.sin(Theta)  # Componente y de las coordenadas cartesianas

# Calculamos la función de corriente ψ
# ψ describe las líneas de corriente del flujo en la esquina
psi = 2 * R**2 * np.sin(2 * Theta)

# Calculamos las componentes del campo de velocidades en coordenadas polares
# Las fórmulas derivan de las propiedades de la función de corriente
v_r = (1 / R) * 4 * R**2 * np.cos(2 * Theta)  # Componente radial de la velocidad
v_theta = -4 * R * np.sin(2 * Theta)  # Componente angular de la velocidad

# Evitamos posibles problemas de indefinición en r = 0
# En r = 0, asignamos v_r = 0 y v_theta = 0 para evitar divisiones por cero
v_r[R == 0] = 0
v_theta[R == 0] = 0

# Convertimos las velocidades a coordenadas cartesianas
# Usamos las relaciones entre coordenadas polares y cartesianas
U = v_r * np.cos(Theta) - v_theta * np.sin(Theta)  # Componente x de la velocidad
V = v_r * np.sin(Theta) + v_theta * np.cos(Theta)  # Componente y de la velocidad

# Calculamos la magnitud de la velocidad
# Esto nos permite visualizar la intensidad del flujo en cada punto
speed = np.sqrt(U**2 + V**2)

# Graficamos las líneas de corriente
plt.figure(figsize=(8, 6))
plt.contour(X, Y, psi, levels=50, cmap='viridis')  # Contornos de ψ con 50 niveles
plt.title('Líneas de corriente cerca de una esquina de 90°')  # Título del gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('y')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.colorbar(label='Función de corriente ψ')  # Barra de color para ψ
plt.show()

# Graficamos el campo de velocidades con densidad reducida y escala de colores
plt.figure(figsize=(8, 6))
plt.quiver(
    X[::5, ::5], Y[::5, ::5], U[::5, ::5], V[::5, ::5],  # Subconjunto de flechas para reducir densidad
    speed[::5, ::5], cmap='cool'  # Color basado en la magnitud de velocidad
)
plt.title('Campo de velocidades cerca de una esquina de 90° (con magnitud)')  # Título del gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('y')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.colorbar(label='Magnitud de velocidad [m/s]')  # Barra de color para la magnitud de velocidad
plt.show()
