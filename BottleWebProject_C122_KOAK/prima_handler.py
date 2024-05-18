from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph

@post('/prima_result', method='POST')
def getResult():
    size = int(request.forms.get('matrix_size'))
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if request.forms.get('matrix[%i][%i]'%(i, j)) == "":
                if(i != j):
                    matrix[i, j] = -1
                else:
                    matrix[i, j] = 0
            else:
                matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
    createGraph.createGraph(matrix, [])
    print(matrix)
    return template('result.tpl',title='Prima method result',
        message='Ниже представлен ваш граф, вычисленный по алгоритму Прима.',
        year=datetime.now().year, data=matrix)


