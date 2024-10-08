import numpy as np
import numpy as np

# Angles for the 16 states
angles = np.array([
    [36, 84, 151, 38],
    [36, 84, 196, 38],
    [81, 84, 196, 38],
    [81, 84, 151, 38],
    [81, 129, 151, 38],
    [81, 129, 196, 38],
    [58.5, 129, 196, 38],
    [58.5, 129, 151, 38],
    [58.5, 129, 151, -7],
    [58.5, 129, 173.5, -7],
    [81, 129, 173.5, -7],
    [36, 84, 173.5, -7],
    [81, 84, 173.5, -7],
    [81, 84, 196, -7],
    [36, 84, 196, -7],
    [81, 129, 196, -7],
    [36, 129, 196, -7]
])

# Gamma matricies values
Gamma_1 = 0.5 * np.array([[0, 1, 0, 0],
                          [1, 0, 0, 0],
                          [0, 0, 0, 1],
                          [0, 0, 1, 0]])

Gamma_2 = 0.5 * np.array([[0, -1j, 0, 0],
                          [1j, 0, 0, 0],
                          [0, 0, 0, -1j],
                          [0, 0, 1j, 0]])

Gamma_3 = 0.5 * np.array([[1, 0, 0, 0],
                          [0, -1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, -1]])

Gamma_4 = 0.5 * np.array([[0, 0, 1, 0],
                          [0, 0, 0, 1],
                          [1, 0, 0, 0],
                          [0, 1, 0, 0]])

Gamma_5 = 0.5 * np.array([[0, 0, 0, 1],
                          [0, 0, 1, 0],
                          [0, 1, 0, 0],
                          [1, 0, 0, 0]])

Gamma_6 = 0.5 * np.array([[0, 0, 0, -1j],
                          [0, 0, 1j, 0],
                          [0, -1j, 0, 0],
                          [1j, 0, 0, 0]])

Gamma_7 = 0.5 * np.array([[0, 0, 1, 0],
                          [0, 0, 0, -1],
                          [1, 0, 0, 0],
                          [0, -1, 0, 0]])

Gamma_8 = 0.5 * np.array([[0, 0, -1j, 0],
                          [0, 0, 0, -1j],
                          [1j, 0, 0, 0],
                          [0, 1j, 0, 0]])

Gamma_9 = 0.5 * np.array([[0, 0, 0, -1j],
                          [0, 0, -1j, 0],
                          [0, 1j, 0, 0],
                          [1j, 0, 0, 0]])

Gamma_10 = 0.5 * np.array([[0, 0, 0, -1],
                           [0, 0, 1, 0],
                           [0, 1, 0, 0],
                           [-1, 0, 0, 0]])

Gamma_11 = 0.5 * np.array([[0, 0, -1j, 0],
                           [0, 0, 0, 1j],
                           [1j, 0, 0, 0],
                           [0, -1j, 0, 0]])

Gamma_12 = 0.5 * np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, -1, 0],
                           [0, 0, 0, -1]])

Gamma_13 = 0.5 * np.array([[0, 1, 0, 0],
                           [1, 0, 0, 0],
                           [0, 0, 0, -1],
                           [0, 0, -1, 0]])

Gamma_14 = 0.5 * np.array([[0, -1j, 0, 0],
                           [1j, 0, 0, 0],
                           [0, 0, 0, 1j],
                           [0, 0, -1j, 0]])

Gamma_15 = 0.5 * np.array([[1, 0, 0, 0],
                           [0, -1, 0, 0],
                           [0, 0, -1, 0],
                           [0, 0, 0, 1]])

Gamma_16 = 0.5 * np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])

# Array with all the matricies
matrices = [Gamma_1, Gamma_2, Gamma_3, Gamma_4, Gamma_5, Gamma_6, Gamma_7, Gamma_8, Gamma_9, Gamma_10, Gamma_11, Gamma_12, Gamma_13, Gamma_14, Gamma_15, Gamma_16]

# Well-known vector
hh = np.array([[1], [0], [0], [0]])
hv = np.array([[0], [1], [0], [0]])
vh = np.array([[0], [0], [1], [0]])
vv = np.array([[0], [0], [0], [1]])

# N for phi-
n = np.array([5285, 94, 5259, 28, 2237, 3064, 3133, 2002, 3074, 430, 3013, 2027, 2759, 2412, 2517, 516, 4681])
n_complex = np.array(n, dtype=np.complex128)