import unittest
import daykstra_calculations
import math

correct_matrixes = [[[0, 1, 5], [1, 0, 2], [5, 2, 0]], 
                    [[0, 1, 5, 42, 18], [1, 0, math.inf, 6, math.inf ], [5, math.inf, 0, math.inf, 3], [42, 6, math.inf,0 , math.inf], [18, math.inf, 3, math.inf, 0]],
                    [[0, 10, 10, 5, 7, 16], [10, 0, 9, 9, 14, 11 ], [10, 9, 0, 4, 8, 18], [5, 9, 4, 0, 9, 4], [7, 14, 8, 9, 0, 3], [16, 11, 18, 4, 3, 0]],
                    [[0, math.inf, math.inf, 17], [math.inf, 0, 5, 18], [math.inf, 5, 0, 13], [17, 18, 13, 0]], 
                    [ [0, 13, 10, 11, 9, 14, 11, 17, 15, 0], [13, 0, 12, 17, 7, 18, 4, 9, 11, 8], [10, 12, 0, 15, 8, 15, 7, 3, 7, 14], [11, 17, 15, 0, 2, 9, 16, 15, 19, 6], [9, 7, 8, 2, 0, 17, 14, 7, 3, 1], [14, 18, 15, 9, 17, 0, 0, 2, 9, 10], [11, 4, 7, 16, 14, 0, 0, 15, 12, 15], [17, 9, 3, 15, 7, 2, 15, 0, 6, 5], [15, 11, 7, 19, 3, 9, 12, 6, 0, 15], [0, 8, 14, 6, 1, 10, 15, 5, 15, 0] ]]

correct_add_data = [[3, 2], [5, 1], [6, 5], [4, 0], [10, 4]]

answers = [ [3, 2, 0], 
            [1, 0, 6, 6, 9],
            [9, 11, 8, 4, 3, 0],
            [0, 35, 30, 17], 
            [1, 7, 8, 2, 0, 8, 8, 6, 3, 1]]

class Test_test_DaykstraMethod(unittest.TestCase):
    def test_correctData(self):
        for (matrixT, addDataT, AnswerT) in zip(correct_matrixes, correct_add_data, answers):
            self.assertEquals(daykstra_calculations.Dijkstra(addDataT[0], addDataT[1], matrixT), AnswerT, msg = f"Error in: {matrixT}")
        
    def test_incorrectDataWithException(self):
        incorrect_add_data = [[3, 2], [5, 7], [7, 5], [4, -1], [-1, 4]]
        with self.assertRaises(IndexError): 
            for (matrixT, addDataT) in zip(correct_matrixes, incorrect_add_data):
                daykstra_calculations.Dijkstra(addDataT[0], addDataT[1], matrixT)
                
    def test_incorrectMatrix(self):
        incorrect_matrixes =  [[ [1, 0, 2], [5, 2, 0]], 
                    [[0, 1, 5, 42, 18], [1, 0, math.inf, 6, math.inf ], [5, math.inf, 0, math.inf, 3], [42, 6, math.inf,0 , math.inf], [18, math.inf, 3, math.inf, 0]],
                    [[0, 10, 10, 5, 7, 16], [10, 0, 9, 9, 14, 11 ], [10, 9, 0, 4, 8, 18], [5, 9, 4, 0, 9, 4], [7, 14, 8, 9, 0, 3], [16, 11, 18, 4, 3, 0], [16, 11, 18, 4, 3, 0]],
                    [[0, math.inf, math.inf, 17], [math.inf, 0, 5, 18], [math.inf, 5, 13], [17, 18, 13, 0]], 
                    [[13, 0, 12, 17, 7, 18, 4, 9, 11, 8], [10, 12, 0, 15, 8, 15, 7, 3, 7, 14], [11, 17, 15, 0, 2, 9, 16, 15, 19, 6], [9, 7, 8, 2, 0, 17, 14, 7, 3, 1], [14, 18, 15, 9, 17, 0, 0, 2, 9, 10], [11, 4, 7, 16, 14, 0, 0, 15, 12, 15], [17, 9, 3, 15, 7, 2, 15, 0, 6, 5], [15, 11, 7, 19, 3, 9, 12, 6, 0, 15], [0, 8, 14, 6, 1, 10, 15, 5, 15, 0] ]]
        with self.assertRaises(IndexError): 
            for (matrixT, addDataT) in zip(incorrect_matrixes, correct_add_data):
                daykstra_calculations.Dijkstra(addDataT[0], addDataT[1], matrixT)

    def test_incorrectDataWithoutException(self):
        incorrect_add_data = [[3, 1], [5, 0], [6, 2], [3, 0], [10, 5]]
        for (matrixT, addDataT, AnswerT) in zip(correct_matrixes, incorrect_add_data, answers):
            self.assertNotEquals(daykstra_calculations.Dijkstra(addDataT[0], addDataT[1], matrixT), AnswerT, msg = f"Error in: {matrixT}")

if __name__ == '__main__':
    unittest.main()
