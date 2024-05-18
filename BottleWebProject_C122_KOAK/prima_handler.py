from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph  # импорт модуля для создания графов
import save_history

@post('/prima_result', method='POST')  # обработка post-запросов
#  функция для получения результатов вычислений
def getResult():
    size = int(request.forms.get('matrix_size'))  # получаем размерность матрицы
    matrix = np.zeros((size, size))  # создание новой матрицы размера size x size и заполнение ее нулями
    # перебор элементов матрицы
    for i in range(size):
        for j in range(size):
            # Проверяем, что значение было введено
            if request.forms.get('matrix[%i][%i]'%(i, j)) == "":
                # Если не была введено значение между вершинами - присваиваем -1
                if(i != j):
                    matrix[i, j] = -1
                # Иначе - 0
                else:
                    matrix[i, j] = 0
            else:
              matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))  # получаем элементы матрицы, введенные на странице калькулятора
    
    edge_list, mst = prim_mst(matrix)  # вызов метода для нахождения mst и суммарного веса mst

    save_history.createhistory("Prima", [edge_list, mst])
    

    createGraph.createGraph(matrix, edge_list)  # создание нового графа

    return template('result.tpl',title='Prima method result',
        message='Ниже представлен ваш граф, вычисленный по алгоритму Прима.',
        year=datetime.now().year, data=mst)  # открытие страницы с результатами

# функция для нахождения наименьшего остовного дерева алгоритмом Прима
def prim_mst(matrix):
    size = len(matrix)  # определение размера матрицы
    visited = [False] * size  # список посещенных вершин
    parent = [None] * size  # список с информацией о вершине-родителе для текущей вершины
    edge_list = []  # инициализация пустого списка, в котором будут ребра наименьшего остовного дерева
    mst = 0;

    # стартовая вершина
    start_vertex = 0  # выбор стартовой вершины
    visited[start_vertex] = True  # отмечаем вершину посещенной

    # основной цикл алгоритма Прима
    for _ in range(size - 1):
        min_weight = float('inf')  # инициализация переменной для хранения минимального веса ребра значением, представляющим бесконечность
        # цикл для прохода по всем вершинам графа
        for i in range(size):
            if visited[i]:  # проверка на то, была ли посещена текущая вершина
                # проверяем все соседние вершины для текущей
                for j in range(size):
                    # проверяем, что вершина была посещена, существует ли между i и j вершинами ребро
                    # и также проверяем является ли вес текущего ребра меньше, чем текущее минимальное значение
                    if not visited[j] and matrix[i][j] > 0 and matrix[i][j] < min_weight:
                        min_weight = matrix[i][j]  # обновляем минимальное значение
                        min_i, min_j = i, j  # запись индексов текущих вершин в min_i и min_j

        visited[min_j] = True  # отмечаем вершину min_j как посещенную
        parent[min_j] = min_i  # обновление родителя для вершины min_j в списке
        edge_list.append((min_i + 1, min_j + 1))  # добавляем ребро в список ребер минималльного остовного дерева
        mst+=min_weight;  # обновление суммарного веса искомого mst

    return edge_list, mst

                        


