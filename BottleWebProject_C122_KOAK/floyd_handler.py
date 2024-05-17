from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph

@post('/floyd_result', method='POST')
def getResult():
    size = int(request.forms.get('matrix_size'))
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
    matrix = floydmethod(matrix)
    createGraph.createGraph(matrix, [])
    return template('result.tpl',title='Floyd method result',
        message='Ниже представлен ваш граф, вычисленный по методу Флойда.',
        year=datetime.now().year, data=matrix)

def floydmethod(V):

    N = len(V)


    P = [[v for v in range(N)] for u in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d = V[i][k] + V[k][j]
                if V[i][j] > d:
                    V[i][j] = d
    return V