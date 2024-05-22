import unittest
import prima_handler

class Test_test_prima_edge_list(unittest.TestCase):
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
        results=[[(1, 2), (2, 3), (3,4)], [(1, 2), (2, 3)], [(1, 2), (1, 3)],
                [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)],
                [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)],
                [(1, 2), (2, 3), (3, 4), (2, 5)]
                ]
        for matrix, result in zip(matrices, results):
            self.assertEquals(prima_handler.prim_mst(matrix)[0], result, msg=f'Test faild with matrrix {matrix}')
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
         [0, 0, 1, 0]],
         
         [[0, 1],
         [1, 0]]
         ]
        results=[[], [(1,2), (1,2), (1,2)], [(1,2), (1,3), (2, 4)], [(1, 2), (2, 3), (2, 3), (2, 3)],
              [(1, 2), (2, 3), (3, 4)], [(1, 2)]]
        
        for matrix, result in zip(matrices, results):
            self.assertEquals(prima_handler.prim_mst(matrix)[0], result, msg=f'Test faild with matrix: {matrix}')
    
    def test_exceptions(self):
        matrices = [[], 
                    
         [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
         
         [[0, -1, 0, 0],
         [-1, 0, 1, 0],
         [0, 1, 0, 1],
         [0, 0, 1, 0]],
         
         [[1, 1, 0],
         [1, 0, 1],
         [0, 1, 1],
         [0, 0, 1]]
         ]
        results = [IndexError, UnboundLocalError, UnboundLocalError, IndexError]
        for (matrix, result) in zip(matrices, results):
            try:
                prima_handler.prim_mst(matrix)
            except result:
                pass
            except Exception as e:
                self.fail(f'Test faild with matrix {matrix}. Got {e.__class__.__name__} instead of {result.__name__}.')
            else:
                self.fail(f'Test faild with matrix {matrix}: the exception was not caused')
if __name__ == '__main__':
    unittest.main()
