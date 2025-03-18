import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 10

P1 =(-0.5 * n, -0.5 * n, -0.5 * n)
P2 =(-0.5 * n, -0.5 * n, 0.5 * n)
P3 =(-0.5 * n, 0.5 * n, -0.5 * n)
P4 =(-0.5 * n, 0.5 * n, 0.5 * n)
P5 =(0.5 * n, -0.5 * n, -0.5 * n)
P6 =(0.5 * n, -0.5 * n, 0.5 * n)
P7 =(0.5 * n, 0.5 * n, -0.5 * n)
P8 =(0.5 * n, 0.5 * n, 0.5 * n)


arestas = [(P1, P2), (P2, P4), (P4, P3), (P3, P1),
(P5, P6), (P6, P8), (P8, P7), (P7, P5),
(P1, P5), (P2, P6), (P3, P7), (P4, P8)]

fig = plt.figure() # Criando uma figura
ax = fig.add_subplot(projection='3d') # Adicionando um subplot tridimensional à figura
# Plotando as arestas do cubo
for aresta in arestas:
  ponto1 = aresta[0] # Obtendo as coordenadas do primeiro ponto da aresta (x,y,z)
  ponto2 = aresta[1] # Obtendo as coordenadas do segundo ponto da aresta (x,y,z)
  # Plotando uma linha entre os dois pontos para representar a aresta
  ax.plot([ponto1[0], ponto2[0]], [ponto1[1], ponto2[1]], [ponto1[2], ponto2[2]], 'r')
#Coordenadas 3D (x,y,z)
# Configurações do gráfico 3D
ax.set_xlabel('X') # Configurando o rótulo do eixo x
ax.set_ylabel('Y') # Configurando o rótulo do eixo y
ax.set_zlabel('Z') # Configurando o rótulo do eixo z
ax.set_title('Cubo no Espaço 3D') # Configurando o título do gráfico
ax.set_xlim(-1 * n, 1 * n) # Limites do eixo X
ax.set_ylim(-1 * n, 1 * n) # Limites do eixo Y
ax.set_zlim(-1 * n, 1 * n) # Limites do eixo Z
# Adicionando manualmente uma legenda para o eixo Z
ax.text(-1, 1.5, 0.5, 'Z', color='black') # Adicionando o texto 'Z' na posição desejada
# Mostrando o gráfico
plt.show()
