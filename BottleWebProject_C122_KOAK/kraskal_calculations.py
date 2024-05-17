from bottle import route, run, template, post, request
from datetime import datetime
import numpy as np
import createGraph

def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

def union_parent(parent, rank, x, y):
    x_root = find_parent(parent, x)
    y_root = find_parent(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kraskal(matrix):
    n = len(matrix)
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    edges = []
    result = []
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != -1:
                edges.append((matrix[i][j], i, j))
    edges.sort()
    for edge in edges:
        weight, x, y = edge
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, rank, x, y)
            result.append([x+1, y+1])
    return result

@post('/kraskal_result', method='POST')
def getResult():
    size = int(request.forms.get('matrix_size'))
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = int(request.forms.get('matrix[%i][%i]'%(i, j)))
    createGraph.createGraph(matrix, kraskal(matrix))
    return template('result.tpl',title='Kraskal method result',
        message='Ниже представлен ваш граф, вычисленный по алгоритму Краскала.',
        year=datetime.now().year, data=matrix)

