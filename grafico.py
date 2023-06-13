import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir os pontos no sistema de coordenadas cilíndricas
r = np.array([1, 2, 3])  # Raio
theta = np.array([np.pi/4, np.pi/2, 3*np.pi/4])  # Ângulo azimute
h = np.array([0, 1, 2])  # Altura

# Converter coordenadas cilíndricas para cartesianas
x = r * np.cos(theta)
y = r * np.sin(theta)
z = h

# Criar uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar os pontos no gráfico
ax.scatter(x, y, z, c='r', marker='o')

# Configurar os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Definir limites dos eixos
ax.set_xlim([-max(r)-1, max(r)+1])
ax.set_ylim([-max(r)-1, max(r)+1])
ax.set_zlim([min(h)-1, max(h)+1])

# Mostrar o gráfico
plt.show()
