import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definir os vértices do cubo
vertices = np.array([
    [-1, -1, -1],  # Vértice 1
    [1, -1, -1],   # Vértice 2
    [1, 1, -1],    # Vértice 3
    [-1, 1, -1],   # Vértice 4
    [-1, -1, 1],   # Vértice 5
    [1, -1, 1],    # Vértice 6
    [1, 1, 1],     # Vértice 7
    [-1, 1, 1]     # Vértice 8
])

# Definir as faces do cubo
faces = np.array([
    [0, 1, 2, 3],  # Face frontal
    [4, 5, 6, 7],  # Face traseira
    [0, 1, 5, 4],  # Face inferior
    [1, 2, 6, 5],  # Face direita
    [2, 3, 7, 6],  # Face superior
    [3, 0, 4, 7]   # Face esquerda
])

# Criar uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotar as faces do cubo
for face in faces:
    polygon = Poly3DCollection([vertices[face]])
    ax.add_collection3d(polygon)

# Configurar os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Definir limites dos eixos
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Mostrar o gráfico
plt.show()
