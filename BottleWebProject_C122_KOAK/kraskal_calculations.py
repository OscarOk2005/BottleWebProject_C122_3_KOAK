# Импортируем необходимые библиотеки и модули
from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph

# Функция для поиска корневого элемента для узла i
def find_parent(parent, i):
    # Если родительский элемент для i не равен i,
    # то рекурсивно вызываем find_parent для родительского элемента
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    # Возвращаем родительский элемент для i
    return parent[i]

# Функция для объединения двух поддеревьев с корневыми элементами x и y
def union_parent(parent, rank, x, y):
    # Находим корневые элементы для x и y
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    # Сравниваем ранги корневых элементов x и y
    if rank[x_root] < rank[y_root]:
        # Если ранг x_root меньше, то присваиваем y_root родительским элементом для x_root
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        # Если ранг y_root меньше, то присваиваем x_root родительским элементом для y_root
        parent[y_root] = x_root
    else:
        # Если ранги равны, то присваиваем x_root родительским элементом для y_root
        # и увеличиваем ранг x_root на 1
        parent[y_root] = x_root
        rank[x_root] += 1

# Функция для нахождения минимального остовного дерева с помощью алгоритма Краскала
def kraskal(matrix):
    # Получаем размерность матрицы
    n = len(matrix)
    # Создаем список parent, в котором каждый элемент является родителем для соответствующего узла
    parent = [i for i in range(n)]
    # Создаем список rank, в котором каждый элемент соответствует рангу узла в поддереве
    rank = [0 for _ in range(n)]
    # Создаем список edges, в котором будем хранить все ребра графа
    edges = []
    # Создаем список result, в котором будем хранить ребра минимального остовного дерева
    result = []
    # Создаем переменную mst, в которой будем хранить суммарный вес ребер минимального остовного дерева
    mst = 0

    # Проходимся по всем элементам матрицы, начиная с первой строки и первого столбца
    for i in range(n):
        for j in range(i+1, n):
            # Если элемент матрицы не равен -1 (т.е. соответствует ребру графа),
            # то добавляем его в список edges в виде кортежа (вес ребра, номер вершины 1, номер вершины 2)
            if matrix[i][j] != -1:
                edges.append((matrix[i][j], i, j))

    # Сортируем список edges по возрастанию весов ребер
    edges.sort()

    # Проходимся по отсортированному списку edges
    for edge in edges:
        # Разбираем кортеж edge на его элементы: вес ребра, номер вершины 1, номер вершины 2
        weight, x, y = edge
        # Если родительские элементы для x и y не равны (т.е. они принадлежат разным поддеревьям),
        # то объединяем эти поддеревья с помощью функции union_parent,
        # добавляем ребро в список result и увеличиваем mst на вес ребра
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, rank, x, y)
            result.append([x+1, y+1])
            mst += weight

    # Возвращаем список result (ребра минимального остовного дерева) и суммарный вес mst
    return result, mst

# Функция для поиска корневого элемента для узла i
def find_parent(parent, i):
    # Если родительский элемент для i не равен i,
    # то рекурсивно вызываем find_parent для родительского элемента
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    # Возвращаем родительский элемент для i
    return parent[i]

# Функция для объединения двух поддеревьев с корневыми элементами x и y
def union_parent(parent, rank, x, y):
    # Находим корневые элементы для x и y
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    # Сравниваем ранги корневых элементов x и y
    if rank[x_root] < rank[y_root]:
        # Если ранг x_root меньше, то присваиваем y_root родительским элементом для x_root
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        # Если ранг y_root меньше, то присваиваем x_root родительским элементом для y_root
        parent[y_root] = x_root
    else:
        # Если ранги равны, то присваиваем x_root родительским элементом для y_root
        # и увеличиваем ранг x_root на 1
        parent[y_root] = x_root
        rank[x_root] += 1

# Функция для нахождения минимального остовного дерева с помощью алгоритма Краскала
def kraskal(matrix):
    # Получаем размерность матрицы
    n = len(matrix)
    # Создаем список parent, в котором каждый элемент является родителем для соответствующего узла
    parent = [i for i in range(n)]
    # Создаем список rank, в котором каждый элемент соответствует рангу узла в поддереве
    rank = [0 for _ in range(n)]
    # Создаем список edges, в котором будем хранить все ребра графа
    edges = []
    # Создаем список result, в котором будем хранить ребра минимального остовного дерева
    result = []
    # Создаем переменную mst, в которой будем хранить суммарный вес ребер минимального остовного дерева
    mst = 0

    # Проходимся по всем элементам матрицы, начиная с первой строки и первого столбца
    for i in range(n):
        for j in range(i+1, n):
            # Если элемент матрицы не равен -1 (т.е. соответствует ребру графа),
            # то добавляем его в список edges в виде кортежа (вес ребра, номер вершины 1, номер вершины 2)
            if matrix[i][j] != -1:
                edges.append((matrix[i][j], i, j))

    # Сортируем список edges по возрастанию весов ребер
    edges.sort()

    # Проходимся по отсортированному списку edges
    for edge in edges:
        # Разбираем кортеж edge на его элементы: вес ребра, номер вершины 1, номер вершины 2
        weight, x, y = edge
        # Если родительские элементы для x и y не равны (т.е. они принадлежат разным поддеревьям),
        # то объединяем эти поддеревья с помощью функции union_parent,
        # добавляем ребро в список result и увеличиваем mst на вес ребра
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, rank, x, y)
            result.append([x+1, y+1])
            mst += weight

    # Возвращаем список result (ребра минимального остовного дерева) и суммарный вес mst
    return result, mst

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
            # Проверяем, что значение было введено
            if request.forms.get('matrix[%i][%i]'%(i, j)) == "":
                # Если не была введено значение между вершинами - присваиваем -1
                if(i != j):
                    matrix[i, j] = -1
                # Иначе - 0
                else:
                    matrix[i, j] = 0
            else:
                matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
    createGraph.createGraph(matrix, kraskal(matrix))
    return template('result.tpl',title='Kraskal method result',
        message='Ниже представлен ваш граф, вычисленный по алгоритму Краскала.',
        year=datetime.now().year, data=matrix)

    # Получение значений работы алгоритма Краскала
    result, mst = kraskal(matrix)
    
    # Создаем граф и получаем результат работы алгоритма Краскала
    createGraph.createGraph(matrix, result)

    # Возвращаем шаблон result.tpl с заданными параметрами title, message, year и data
    return template('result.tpl',title='Kraskal method result',
                     message='Ниже представлен ваш граф, вычисленный по алгоритму Краскала.',
                     year=datetime.now().year, data=mst)