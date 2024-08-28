import numpy as np

# Function to select a matrix by index
def select_matrix(matrices, index):
    """
    Selects a specific matrix from a list of matrices based on the given index.

    :param matrices: List of matrices (NumPy arrays).
    :param index: The index of the matrix to select.
    :return: The selected matrix.
    """
    if index < 0 or index >= len(matrices):
        raise IndexError("Index out of range")
    
    return matrices[index]
