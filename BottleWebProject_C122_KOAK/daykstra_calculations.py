from bottle import route, run, template, post
from datetime import datetime



@post('/daykstra_algorithm_calc', method='GET')

def getResult():
    matrix = ([[0, 7, 8, -1, -1, -1],
                      [7, 0, 11, 2, -1, -1],
                      [8, 11, 0, 6, 9, -1],
                      [-1, 2, 6, 0, 11, 9],
                      [-1, -1, 9, 11, 0, 10],
                      [-1, -1, -1, 9, 10 ,0]])
    return matrix
