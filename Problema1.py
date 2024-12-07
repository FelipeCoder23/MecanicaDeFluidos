# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# Problema 1: Vórtice
# ================================================================

# Este código grafica las líneas de corriente, el campo de velocidades y la función potencial de un vórtice.
# La función de corriente se define como ψ = ln(x^2 + y^2), y se calculan las derivadas correspondientes.

# Definimos el dominio en el plano cartesiano
x = np.linspace(-1, 1, 200)  # Rango de valores de x
y = np.linspace(-1, 1, 200)  # Rango de valores de y
X, Y = np.meshgrid(x, y)  # Generamos una malla de puntos en el plano xy

# Calculamos la función de corriente ψ
# ψ representa las líneas de corriente y depende de la distancia radial al origen
psi = np.log(X**2 + Y**2 + 1e-10)  # Se agrega un término pequeño para evitar logaritmos de cero

# Calculamos el potencial φ
# φ describe el potencial asociado al flujo del vórtice
phi = np.arctan2(Y, X)  # Calculamos φ usando la función arctan2 para manejar signos correctamente

# Calculamos las componentes del campo de velocidades (vx, vy)
# Estas se derivan de las expresiones para un vórtice ideal
U = -2 * Y / (X**2 + Y**2 + 1e-10)  # Componente horizontal de la velocidad
V = 2 * X / (X**2 + Y**2 + 1e-10)   # Componente vertical de la velocidad

# Graficamos las líneas de corriente
plt.figure(figsize=(8, 6))
plt.contour(X, Y, psi, levels=50, cmap='viridis')  # Contornos de ψ con 50 niveles
plt.title('Líneas de corriente de un vórtice')  # Título del gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('y')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.colorbar(label='Función de corriente ψ')  # Barra de color para ψ
plt.show()

# Graficamos el campo de velocidades con un streamplot
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, U, V, density=2, color='blue')  # Trazamos las líneas de flujo
plt.title('Campo de velocidades de un vórtice')  # Título del gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('y')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.show()

# Graficamos la función potencial φ
plt.figure(figsize=(8, 6))
plt.contour(X, Y, phi, levels=50, cmap='plasma')  # Contornos de φ con 50 niveles
plt.title('Función potencial φ de un vórtice')  # Título del gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('y')  # Etiqueta del eje y
plt.axis('equal')  # Igualamos las proporciones en ambos ejes
plt.colorbar(label='Función potencial φ')  # Barra de color para φ
plt.show()
