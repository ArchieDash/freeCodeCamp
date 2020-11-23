import numpy as np

def calculate(list):
    try:
        matrix = np.array(list).reshape(3,3)
    except:
        raise ValueError("List must contain nine numbers.")
        
    calculations = {
        "mean" : [
                    [np.mean(column) for column in matrix.T],
                    [np.mean(row) for row in matrix],
                    np.mean(matrix.flatten())
                ],

        "variance" : [
                        [np.var(column) for column in matrix.T],
                        [np.var(row) for row in matrix],
                        np.var(matrix.flatten())
                    ],

        "standard deviation": [
                                [np.std(column) for column in matrix.T],
                                [np.std(row) for row in matrix],
                                np.std(matrix.flatten())
                            ],

        "max": [
                [max(column) for column in matrix.T],
                [max(row) for row in matrix],
                max(matrix.flatten())
                ],

        "min": [
                [min(column) for column in matrix.T],
                [min(row) for row in matrix],
                min(matrix.flatten()),
                ],

        "sum": [
                [sum(column) for column in matrix.T],
                [sum(row) for row in matrix],
                sum(matrix.flatten())
                ]
                    }
    return calculations

print(calculate([0,1,2,3,4,5,6,7,8,]))