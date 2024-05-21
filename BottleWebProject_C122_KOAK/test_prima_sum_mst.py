import unittest
import prima_handler
import math

class Test_test_prima_sum_mst(unittest.TestCase):
    def test_correct_data(self):
        matrices = [[[0, 1, 0, 0],
                     [1, 0, 1, 0],
                     [0, 1, 0, 1],
                     [0, 0, 1, 0]],
                    
                    [[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]],
                    
                    [[0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]],
                    
                    [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]],
                     
                     [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
                     
                     [[0, 2, 5, 0, 0],
                      [2, 0, 1, 3, 4],
                      [5, 1, 0, 2, 0],
                      [0, 3, 2, 0, 5],
                      [0, 4, 0, 5, 0]]
                    ]
        results=[3, 2, 2, 9, 9,9]
        for matrix, result in zip(matrices, results):
            self.assertEquals(prima_handler.prim_mst(matrix)[1], result, msg=f'Test faild with matrrix {matrix}')
    def test_uncorrect_data(self):
        matrices=[[0],
                  
         [[0, 1, 0, 0],
         [1, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]],
         
         [[0, 1, 1, 0],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [0, 1, 1, 0]],
         
         [[0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]],
        
        [[1, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 1, 1],
         [0, 0, 1, 0]]
         ]
        results=[0, math.inf, 3, math.inf, 3]
        
        for matrix, result in zip(matrices, results):
            self.assertEquals(prima_handler.prim_mst(matrix)[1], result, msg=f'Test faild with matrix: {matrix}')
if __name__ == '__main__':
    unittest.main()
