import unittest
import math
import floyd_handler

class Test_test_floyda_algorithm(unittest.TestCase):
    def test_correct_data(self):
        original_matrix = [
            [[0, 10, 13, 2], [10, 0, 18, 4], [13, 18, 0, math.inf], [2, 4, math.inf, 0]],
            [
                [0, 8, math.inf, math.inf, 9, math.inf, 14, math.inf, 4, 3], 
                [8, 0, 8, 11, math.inf, math.inf,  math.inf,  math.inf, 6,  math.inf],
                [math.inf, 8, 0, 9, 10, math.inf, math.inf, 5, math.inf, 1],
                [math.inf, 11, 9, 0, math.inf, math.inf, 2, math.inf, math.inf, 10],
                [9, math.inf, 10, 5, 0, 8, 10, math.inf, 8, math.inf],
                [math.inf, math.inf, math.inf, math.inf, math.inf, 0, 3, 9, 10, 5],
                [14, math.inf, math.inf, 2, 10, 3, 0, math.inf, 9, math.inf],
                [4, 6, math.inf, math.inf, 8, 9, 9, 0, math.inf, math.inf],
                [4, 6, math.inf, math.inf, 8, 10, 9, math.inf, 0, 1],
                [3, math.inf, 1, 10, math.inf, 5, math.inf, math.inf, 1, 0]
            ],
            [
                [0, 19, math.inf, 9, 18, 6],
                [19, 0, 10, 17, 17, 6],
                [math.inf, 10, 0, 14, 12, 13],
                [9, 17, 14, 0, 16, 17],
                [18, 17, 12, 16, 0, 8],
                [6, 6, 13, 17, 8, 0]
            ],
            [
                [0, 12, 5, 10, math.inf],
                [12, 0, 4, 11, 6],
                [5, 4, 0, 2, 6],
                [10, 11, 2, 0, math.inf],
                [math.inf, 6, 6, math.inf, 0]
            ],
            [
                [0, 11, 12, 4, 4, math.inf, 8, 3],
                [11, 0, 3, 1, 8, 17, 9, 6],
                [12, 3, 0, math.inf, 16, 14, 18, 17],
                [4, 1, math.inf, 0, 14, 10, 17, 15],
                [4, 8, 16, 14, 0, 14, 18, 10],
                [math.inf, 17, 14, 10, 14, 0, 18, 7],
                [8, 9, 18, 17, 18, 18, 0, 5],
                [3, 6, 17, 15, 10, 7, 5, 0]
            ]
            
        ]
        result_matrix = [
            [[0, 6, 13, 2], [6, 0, 18, 4], [13, 18, 0, 15], [2, 4, 15, 0]],
            [
                [0,	8,	4,	13,	9,	8,	11,	9,	4,	3],
                [8,	0,	8,	11,	14,	12,	13,	13,	6,	7],
                [4,	8,	0,	9,	10,	6,	9,	5,	2,	1],
                [13,	11,	9,	0,	12,	5,	2,	14,	11,	10],
                [9,	14,	10,	5,	0,	8,	7,	15,	8,	9],
                [8,	12,	6,	5,	13,	0,	3,	9,	6,	5],
                [11,	13,	9,	2,	10,	3,	0,	12,	9,	8],
                [4,	6,	8,	11,	8,	9,	9,	0,	8,	7],
                [4,	6,	2,	11,	8,	6,	9,	7,	0,	1],
                [3,	7,	1,	10,	9,	5,	8,	6,	1,	0]
            ],
            [
                [0, 12, 19, 9, 14, 6],
                [12,	0,	10,	17,	14,	6],
                [19,	10,	0,	14,	12,	13],
                [9,	17,	14,	0,	16,	15],
                [14,	14,	12,	16,	0,	8],
                [6,	6,	13,	15,	8,	0]
            ],
            [
                [0,	9,	5,	7,	11],
                [9,	0,	4,	6,	6],
                [5,	4,	0,	2,	6],
                [7,	6,	2,	0,	8],
                [11,	6,	6,	8,	0]
            ],
            [
                [0,	5,	8,	4,	4,	10,	8,	3],
                [5,	0, 3,	1,	8,	11,	9,	6],
                [8,	3,	0,	4,	11,	14,	12,	9],
                [4,	1,	4,	0,	8,	10,	10,	7],
                [4,	8,	11,	8,	0,	14,	12,	7],
                [10, 11, 14, 10, 14, 0,	12,	7],
                [8,	9,	12,	10,	12,	12,	0,	5],
                [3,	6,	9,	7,	7,	7,	5,	0]
            ]
            
        ]
        for i in range(len(original_matrix)):
            self.assertEqual(floyd_handler.floydmethod(original_matrix[i]), result_matrix[i])
        
    def test_incorrectMatrix_Exceptions(self):
        original_matrix = [
            [
                ["a", 4, 5],
                [4, 0, 3],
                [5, 3, 0]
            ],
            [
                [0, 1, 2],
                [1, 0, 5],
                [2, 5, 0],
                [1, 2, 5]
            ],
            [],
            [[0, 5], [5, 0]],
            [
                [0,	8,	4,	13,	9,	8,	11,	9,	4,	3, 5],
                [8,	0,	8,	11,	14,	12,	13,	13,	6,	7, math.inf],
                [4,	8,	0,	9,	10,	6,	9,	5,	2,	1, math.inf],
                [13,	11,	9,	0,	12,	5,	2,	14,	11,	10, math.inf],
                [9,	14,	10,	5,	0,	8,	7,	15,	8,	9, math.inf],
                [8,	12,	6,	5,	13,	0,	3,	9,	6,	5, math.inf],
                [11,	13,	9,	2,	10,	3,	0,	12,	9,	8, math.inf],
                [4,	6,	8,	11,	8,	9,	9,	0,	8,	7, math.inf],
                [4,	6,	2,	11,	8,	6,	9,	7,	0,	1, math.inf],
                [3,	7,	1,	10,	9,	5,	8,	6,	1,	0, math.inf],
                [5, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0]
            ]
        ]
        results = [TypeError, ValueError, IndexError, ValueError, ValueError]
        for i in range(len(original_matrix)):
            try:
                floyd_handler.floydmethod(original_matrix[i])
            except results[i]:
                pass
            else:
                self.fail(f'Not all tests passed!  {original_matrix[i]}' )

if __name__ == '__main__':
    unittest.main()
