# Импортируем необходимые библиотеки и модули
from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph

# Определяем функцию для поиска родителя узла
def find_parent(parent, i):
    # Если родитель узла не равен самому узлу
    if parent[i] != i:
        # Присваиваем родителем узла родителя его родителя (сжатие пути)
        parent[i] = find_parent(parent, parent[i])
    # Возвращаем родителя узла
    return parent[i]

# Определяем функцию для объединения родителей двух узлов
def union_parent(parent, rank, x, y):
    # Находим родителей узлов x и y
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    # Если ранг родителя узла x меньше, чем ранг родителя узла y
    if rank[x_root] < rank[y_root]:
        # Присваиваем родителем узла x родителя узла y
        parent[x_root] = y_root
    # Если ранг родителя узла x больше, чем ранг родителя узла y
    elif rank[x_root] > rank[y_root]:
        # Присваиваем родителем узла y родителя узла x
        parent[y_root] = x_root
    # Если ранги родителей узлов x и y равны
    else:
        # Присваиваем родителем узла y родителя узла x
        parent[y_root] = x_root
        # Увеличиваем ранг родителя узла x
        rank[x_root] += 1

# Определяем функцию, реализующую алгоритм Краскала
def kraskal(matrix):
    # Находим количество вершин в графе (размерность матрицы)
    n = len(matrix)
    # Инициализируем массив родителей (каждый узел является своим родителем)
    parent = [i for i in range(n)]
    # Инициализируем массив рангов (ранг каждого узла равен 0)
    rank = [0 for _ in range(n)]
    # Инициализируем список ребер графа
    edges = []
    # Инициализируем список ребер, включенных в минимальное остовное дерево
    result = []

    # Перебираем все вершины графа (столбцы матрицы)
    for i in range(n):
        # Перебираем все вершины графа, начиная с i+1 (строки матрицы)
        for j in range(i+1, n):
            # Если ребро между вершинами i и j существует (значение в матрице не равно -1)
            if matrix[i][j] != -1:
                # Добавляем ребро в список ребер графа
                edges.append((matrix[i][j], i, j))

    # Сортируем список ребер графа по возрастанию веса
    edges.sort()

    # Перебираем все ребра графа в отсортированном порядке
    for edge in edges:
        # Извлекаем вес ребра и номера вершин, которые оно соединяет
        weight, x, y = edge
        # Если родители вершин x и y различны (вершины принадлежат разным компонентам связности)
        if find_parent(parent, x) != find_parent(parent, y):
            # Объединяем родителей вершин x и y
            union_parent(parent, rank, x, y)
            # Добавляем ребро в список ребер, включенных в минимальное остовное дерево
            result.append([x+1, y+1])

    # Возвращаем список ребер, включенных в минимальное остовное дерево
    return result

# Определяем маршрут для обработки POST-запроса на адрес /kraskal_result
@post('/kraskal_result', method='POST')
def getResult():
    # Получаем размерность матрицы из POST-запроса
    size = int(request.forms.get('matrix_size'))
    # Инициализируем матрицу нулями с помощью библиотеки NumPy
    matrix = np.zeros((size, size))
    # Перебираем все ячейки матрицы
    for i in range(size):
        for j in range(size):
            # Получаем значение ячейки из POST-запроса и присваиваем ее матрице
            matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))

    # Создаем граф и получаем результат работы алгоритма Краскала
    createGraph.createGraph(matrix, kraskal(matrix))

    # Возвращаем шаблон result.tpl с заданными параметрами title, message, year и data
    return template('result.tpl',title='Kraskal method result',
                     message='Ниже представлен ваш граф, вычисленный по алгоритму Краскала.',
                     year=datetime.now().year, data=matrix)