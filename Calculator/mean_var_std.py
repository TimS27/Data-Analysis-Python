import numpy as np

def calculate(list):
    while True:
        try:
            matrix = np.array(list).reshape(3,3)
            matrix_flat = np.array(list).reshape(1,9)

            result =    {
                        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix_flat.mean(axis=1)],
                        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix_flat.var(axis=1)],
                        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix_flat.std(axis=1)],
                        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix_flat.max(axis=1)],
                        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix_flat.min(axis=1)],
                        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix_flat.sum(axis=1)]
                        }

        except ValueError:
            raise ValueError("List must contain nine numbers.")
        else:
            return result