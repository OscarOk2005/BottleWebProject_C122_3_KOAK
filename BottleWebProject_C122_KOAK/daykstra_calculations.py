from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph
import save_history

@post('/daykstra_result', method='POST')
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
    start_node = int(request.forms.get('start_point')) - 1
    save_history.createhistory("Daykstra", [matrix, Dijkstra(size ,start_node, matrix)])
    new_Matrix = Dijkstra(size ,start_node, matrix)
    matrix = np.zeros((size, size))
    for i in range(size):
        matrix[0, i]  = new_Matrix[i]
        matrix[i, 0]  = new_Matrix[i]
    print (matrix)
    createGraph.createGraph(matrix, [])
    return template('result.tpl',title='Daykstra method result',
        message='Ниже представлен ваш граф, вычисленный по методу Дейкстры.',
        year=datetime.now().year, data=matrix)

def Dijkstra(N, S, matrix):
	valid = [True]*N        
	weight = [1000000]*N
	weight[S] = 0
	matrix= np.array(matrix)
	for i in range(N):
		min_weight = 1000001
		ID_min_weight = -1
		for j in range(N):
			if valid[j] and weight[j] < min_weight:
				min_weight = weight[j]
				ID_min_weight = j
		for z in range(N):
			if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
				weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
		valid[ID_min_weight] = False
	return weight