import matplotlib.pyplot as plt
import numpy as np
import utils as ut
from values import *

def a(h, q):
    return (1 / np.sqrt(2)) * (np.sin(2 * h) - 1j * np.sin(2 * (h - q)))

def b(h, q):
    return (1 / np.sqrt(2)) * (np.cos(2 * h) + 1j * np.cos(2 * (h - q)))

def phi(v):
    angle = ut.select_matrix(angles, v-1)
    return a(angles[v-1][0], angles[v-1][1]) * a(angles[v-1][2], angles[v-1][3]) * hh + \
        a(angles[v-1][0], angles[v-1][1]) * b(angles[v-1][2], angles[v-1][3]) * hv + \
        b(angles[v-1][0], angles[v-1][1]) * a(angles[v-1][2], angles[v-1][3]) * vh + \
        b(angles[v-1][0], angles[v-1][1]) * b(angles[v-1][2], angles[v-1][3]) * vv

def B(v, u):
    angles = ut.select_matrix(matrices, u-1)
    int_res = np.dot(phi(v).conj().T, angles)
    fin_res = np.dot(int_res, phi(v))
    return fin_res

def N():
    sum = 0
    for i in range(1, 5):
        sum += n_complex[i]
    return sum

def r(v):
    int_res = np.zeros((4, 4), dtype=np.complex128)
    for i in range(1, 17):
       int_res += np.linalg.inv(B(v, i)) * n_complex[i]
    return int_res / N()

def density_m():
    int_res = np.zeros((4, 4), dtype=np.complex128)
    for i in range(1, 17):
        angles = ut.select_matrix(matrices, i-1)
        int_res += np.dot(angles, r(i))
    return int_res

density_matrix = density_m()
print(density_matrix)
