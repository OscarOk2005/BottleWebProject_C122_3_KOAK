import unittest
import kraskal_calculations

class test_kraskal_sum_mst(unittest.TestCase):
    def test_correct_data(self):
        
        matrices = [
            [ [0, 7, 8, -1, -1, -1],
            [7, 0, 11, 2, -1, -1],
            [8, 11, 0, 6, 9, -1],
            [-1, 2, 6, 0, 11, 9],
            [-1, -1, 9, 11, 0, 10],
            [-1, -1, -1, 9, 10 ,0] ],
    
            [ [0, 2, 4, -1, -1, -1],
            [2, 0, 9, 7, -1, -1],
            [4, 9, 0, 8, 1, -1],
            [-1, 7, 8, 0, 3, 1],
            [-1, -1, 1, 3, 0, 2],
            [-1, -1, -1, 1, 2 ,0] ],
    
            [ [0, 2, 4],
            [2, 0, 3],
            [4, 3, 0] ],
    
            [ [0, 2, 4, 6, -1, -1, -1, -1],
            [2, 0, 3, 8, 9, -1, -1, -1],
            [4, 3, 0, 5, 2, 11, -1, -1],
            [6, 8, 5, 0, 7, 4, 13, -1],
            [-1, 9, 2, 7, 0, 3, 1, 14],
            [-1, -1, 11, 4, 3, 0, 2, 5],
            [-1, -1, -1, 13, 1, 2, 0, 12],
            [-1, -1, -1, -1, 14, 5, 12, 0] ],
    
            [ [0, 2, 4, 6, -1, -1, -1, -1, -1],
            [2, 0, 3, 8, 9, -1, -1, -1, -1],
            [4, 3, 0, 5, 2, 11, -1, -1, -1],
            [6, 8, 5, 0, 7, 4, 13, -1, -1],
            [-1, 9, 2, 7, 0, 3, 1, 14, -1],
            [-1, -1, 11, 4, 3, 0, 2, 5, 15],
            [-1, -1, -1, 13, 1, 2, 0, 12, 6],
            [-1, -1, -1, -1, 14, 5, 12, 0, 9],
            [-1, -1, -1, -1, -1, 15, 6, 9, 0] ]
        ]

        results = [
            33, 
            10, 
            5, 
            19, 
            25
        ]
        
        for matrix, result in zip(matrices, results):
            self.assertEqual(kraskal_calculations.kraskal(matrix)[1], result, msg=f'Test faild with matrix: {matrix}')
    
    def test_uncorrect_data(self):
        
        matrices = [
            [0],
                  
            [[0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]],
         
            [[0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0]],
         
            [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]],
        
            [[1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1]]
        ]
        
        results = [
            0, 
            
            0,
            
            1, 
            
            1,
            
            0
        ]
        
        for matrix, result in zip(matrices, results):
            self.assertEquals(kraskal_calculations.kraskal(matrix)[1], result, msg=f'Test faild with matrix: {matrix}')
    
    def test_exceptions(self):
        
        matrices = [
            [], 
            
            [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
         
            [[0, -1, 0],
            [-1, 0, -1],
            [0, -1, 0]],
         
            [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]]
        ]
        
        results = [
            IndexError, 
            UnboundLocalError, 
            UnboundLocalError, 
            IndexError
        ]
        
        for matrix, result in zip(matrices, results):
            try:
                kraskal_calculations.kraskal(matrix)
            except result:
                pass
            except Exception as e:
                self.fail(f'Test faild with matrix {matrix}. Got {e.__class__.__name__} instead of {result.__name__}.')

if __name__ == '__main__':
    unittest.main()