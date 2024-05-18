import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from math import sqrt

# Функция создания графа
# pathes - матрица смежности графа
# color_pathes - список граней, которые необходимо выделить на графе
def createGraph(pathes, color_pathes):
    # Преобразование list в array
    pathes =  np.array(pathes)
    color_pathes =  np.array(color_pathes)
    # Создание графа
    G = nx.Graph()
    # Добавление всех граней из матрицы смежности
    for i in range(int(sqrt(pathes.size))):
        for j in range(int(sqrt(pathes.size))):
            if pathes[i, j] >= 1:
                G.add_edge(i + 1, j + 1, weight=int(pathes[i, j]))
    # Настройка позиционирования элементов
    pos = nx.spring_layout(G, seed=666)
    # Прорисовка граней
    nx.draw_networkx_edges(G, pos, width=2, edge_color="tab:green")
    # Прорисовка вершин
    for i in range(int(sqrt(pathes.size))):
        nx.draw_networkx_nodes(G, pos, nodelist=[i + 1], node_size=900, node_color="tab:red")
    # Выделение необходимых граней цветом
    for i in range (int(color_pathes.size/2)):
        nx.draw_networkx_edges(G, pos, edgelist= [(color_pathes[i][0], color_pathes[i][1])], width=4, edge_color="tab:red")
    # Прорисовка номеров вершин
    nx.draw_networkx_labels(G, pos, font_size=20)
    # Прорисовка весов граней
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    # Сохранение графа в файл
    plt.savefig("static/images/Graph.png", dpi=150)
    # Закрытие работы с графом
    plt.close()
    return
