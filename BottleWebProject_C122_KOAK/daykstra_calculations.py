from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph
import save_history
import math

@post('/daykstra_result', method='POST')
def getResult():
    # Получаем размер матрицы
    size = int(request.forms.get('matrix_size'))
    # Создаём пустую матрицу
    old_matrix = np.zeros((size, size))
    # Заполняем матрицу данными со страницы
    for i in range(size):
        for j in range(size):
             # Проверяем, что значение было введено
            if request.forms.get('matrix[%i][%i]'%(i, j)) == "":
                # Если не была введено значение между вершинами - присваиваем бесконечность
                if(i != j):
                    old_matrix[i, j] = math.inf
                # Иначе - 0
                else:
                    old_matrix[i, j] = 0
            else:
                # Получение данных
                old_matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
   
    # Получение начальной точки
    start_node = int(request.forms.get('start_point')) - 1
    # Получение списка расстояний от указаной точки до других
    intermediate_matrix = Dijkstra(size,start_node, old_matrix)
    # Заполнение новой матрицы
    new_Matrix = np.zeros((size, size))
    for i in range(size):
        new_Matrix[start_node, i]  = intermediate_matrix[i]
        new_Matrix[i, start_node]  = intermediate_matrix[i]
    # Сохранение начальной и итоговой матриц
    save_history.createhistory("Daykstra", [old_matrix.tolist(), new_Matrix.tolist()])
    # Создание графа
    createGraph.createGraph(new_Matrix, [])
    # Переход на страницу с результатом
    return template('result.tpl',title='Daykstra method result',
        message='Ниже представлен ваш граф, вычисленный по методу Дейкстры.',
        year=datetime.now().year, data=new_Matrix)

# Метод алгоритма Дейкстры
# N - Размер матрицы
# S - Начальная вершина
# matrix - матрица смежности
def Dijkstra(N, S, matrix):
    # Создаём массив в котором обозначаем все вершины непроверенными  
	valid = [True]*N      
    # Присваиваем всем вершинам большую стоимость 
	cost = [1000000]*N
    # Присваиваем начальной вершине стоимость 0 
	cost[S] = 0
    # Преобразовываем list в array 
	matrix = np.array(matrix)
    # Перебор всех вершин  
	for i in range(N):
        # Переменная, хранящая минимально найденную стоимость    
		min_weight = 1000001
        # Переменная, хранящая номер вершины с минимальной стоимостью    
		ID_min_weight = -1
        # Поиск вершины с минимальной стоимостью    
		for j in range(N):
            # Ищем вершины с минимальной стоимостью из непроверенных     
			if valid[j] and cost[j] < min_weight:
                # Сохраняем минимальную стоимость и номер вершины с минимальной стоимостью        
				min_weight = cost[j]
				ID_min_weight = j
        # Цикл обновляющий стоимости всех соседних       
		for j in range(N):
            # Если новая стоимость меньше старой -  обновляем её     
			if cost[ID_min_weight] + matrix[ID_min_weight][j] < cost[j]:
				cost[j] = cost[ID_min_weight] + matrix[ID_min_weight][j]
        # Отмечаем точку как проверенную        
		valid[ID_min_weight] = False
    # Возвращаем список длин от исходной точки до остальных    
	return cost