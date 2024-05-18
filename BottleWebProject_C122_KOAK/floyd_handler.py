from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph
import save_history

@post('/floyd_result', method='POST')
def getResult():
    """
    Обрабатывает данные из формы, вычисляет кратчайшие расстояния по алгоритму Флойда-Уоршелла, 
    создает визуализацию графа и возвращает результат на шаблон.
    """
     # Получает размер матрицы из формы
    size = int(request.forms.get('matrix_size'))
    # Создает матрицу нулей размерности size x size
    matrix = np.zeros((size, size))
    # Заполняет матрицу значениями из формы 
    for i in range(size):
        for j in range(size):
            matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
    # Создаёт массив из начальной и итоговой матрицы для сохранения в историю
    savedata = [matrix.tolist(), floydmethod(matrix).tolist()]
    # Вычисляет кратчайшие расстояния между всеми парами вершин
    matrix = floydmethod(matrix)
    # Сохраняет данные в json-файле
    save_history.createhistory("Floyda", savedata)
    # Создает визуализацию графа
    createGraph.createGraph(matrix, [])
    # Возвращает результат на шаблон "result.tpl"
    return template('result.tpl',title='Floyd method result',
        message='Ниже представлен ваш граф, вычисленный по методу Флойда.',
        year=datetime.now().year, data=matrix)

def floydmethod(V):
    """
    Реализует алгоритм Флойда-Уоршелла для вычисления кратчайших расстояний между всеми парами вершин в графе.
    """
    # Получает размер матрицы смежности
    N = len(V)
    
    # Алгоритм Флойда-Уоршелла:
    for k in range(N):
        for i in range(N):
            for j in range(N):
                # Вычисляет кратчайшее расстояние через вершину k
                d = V[i][k] + V[k][j]
                # Если найден более короткий путь, обновляет матрицу расстояний
                if V[i][j] > d:
                    V[i][j] = d
    # Возвращает обновленную матрицу расстояний
    return V