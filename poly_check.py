import sympy as sp
import numpy as np
import matplotlib as plt
from tbcontrol.symbolic import routh


def check_definition(poly_):
    roots = poly_.roots()
    for item in roots:
        if item.real >= 0:
            return False
    return True


def check_Hurwitz(poly_):
    mtr = np.diag(list(poly_)[poly_.degree()-1::-1])
    tmp = list(poly_)[::-1]
    shift = 0
    for i in range(len(mtr)):
        if i % 2 == 0:
            k = 1
        else:
            k = 0
        for j in range(len(mtr)):
            if k < len(tmp):
                mtr[i][j+shift] = tmp[k]
            k += 2
        if i % 2 != 0:
            shift += 1
    if tmp[0] <= 0:
        return False
    for i in range(len(mtr)):
        tmp_mtr = mtr[0:1+i, 0:1+i]
        if np.linalg.det(tmp_mtr) <= 0:
            return False
    return True


def check_Routh(poly_):
    p = sp.Poly(poly_, s)
    res = routh(p)
    res = np.array(res)
    tmp = list(poly_)[::-1]
    if tmp[0] <= 0:
        return False
    for i in range(len(res)):
        if res[i][0] <= 0:
            return False
    return True


def build_trans_func(A, b, c):
    sI = s * sp.eye(2)
    t_mtr = sI - A
    sp.pprint(f'sI-A = {t_mtr}')
    det_t_mtr = sp.det(t_mtr)
    sp.pprint(f'det of trans matrix = {det_t_mtr}')
    t_mtr = t_mtr.inv() * det_t_mtr
    sp.pprint(f'(sI-A).inv = {t_mtr}')
    t_mtr = t_mtr * b
    sp.pprint(f'(sI-A_1).inv * b = {t_mtr}')
    t_mtr = c * t_mtr
    sp.pprint(f'c * (sI-A_1).inv * b = {t_mtr}')
    print('trans matrix = ')
    t_mtr = sp.simplify(t_mtr)
    sp.pprint(t_mtr)
    sp.pprint(1 / det_t_mtr)
    print(t_mtr)


s = sp.symbols('s')

"""Preparation of data 1"""

A_1 = sp.Matrix([[1, 3],
                 [-1, 2]])
b_1 = sp.Matrix([[1],
                 [0]])
c_1 = sp.Matrix([[2, 1]])
print('A_1 = ')
sp.pprint(A_1)
print('b_1 = ')
sp.pprint(b_1)
print('c_1 = ')
sp.pprint(c_1)

"""Computation of transform function W_1"""

build_trans_func(A_1, b_1, c_1)
# sI = s * sp.eye(2)
# t_mtr = sI - A_1
# sp.pprint(f'sI-A_1 = {t_mtr}')
# det_t_mtr = sp.det(t_mtr)
# sp.pprint(f'det of trans matrix = {det_t_mtr}')
# t_mtr = t_mtr.inv() * det_t_mtr
# sp.pprint(f'(sI-A_1).inv = {t_mtr}')
# t_mtr = t_mtr * b_1
# sp.pprint(f'(sI-A_1).inv * b_1 = {t_mtr}')
# t_mtr = c_1 * t_mtr
# sp.pprint(f'c_1 * (sI-A_1).inv * b_1 = {t_mtr}')
# print('trans matrix = ')
# t_mtr = sp.simplify(t_mtr)
# sp.pprint(t_mtr)
# sp.pprint(1 / det_t_mtr)
# print(t_mtr)

"""Stability check W_1"""

poly1 = np.loadtxt('poly1.txt')
poly1 = poly1[::-1]
poly1 = np.polynomial.Polynomial(poly1)
print(poly1)
print(check_definition(poly1))
print(check_Hurwitz(poly1))
print(check_Routh(poly1))

"""Preparation of data 2"""

A_2 = sp.Matrix([[0, 4],
                 [-6, 9]])
b_2 = sp.Matrix([[0],
                 [1]])
c_2 = sp.Matrix([[1, 1]])
print('A_2 = ')
sp.pprint(A_2)
print('b_2 = ')
sp.pprint(b_2)
print('c_2 = ')
sp.pprint(c_2)

"""Computation of transform function W_2"""

build_trans_func(A_2, b_2, c_2)

"""Stability check W_2"""

poly2 = np.loadtxt('poly2.txt')
poly2 = poly2[::-1]
poly2 = np.polynomial.Polynomial(poly2)
print(poly2)
print(check_definition(poly2))
print(check_Hurwitz(poly2))
print(check_Routh(poly2))

"""Stability check W_11"""

poly11 = np.loadtxt('poly11.txt')
poly11 = poly11[::-1]
poly11 = np.polynomial.Polynomial(poly11)
print(poly11)
print(check_definition(poly11))
print(check_Hurwitz(poly11))
print(check_Routh(poly11))

"""Stability check W_22"""

poly22 = np.loadtxt('poly22.txt')
poly22 = poly22[::-1]
poly22 = np.polynomial.Polynomial(poly22)
print(poly22)
print(check_definition(poly22))
print(check_Hurwitz(poly22))
print(check_Routh(poly22))

"""Stability check W_12"""

poly12 = np.loadtxt('poly12.txt')
poly12 = poly12[::-1]
poly12 = np.polynomial.Polynomial(poly12)
print(poly12)
print(check_definition(poly12))
print(check_Hurwitz(poly12))
print(check_Routh(poly12))

"""Stability check W_21"""

poly21 = np.loadtxt('poly21.txt')
poly21 = poly21[::-1]
poly21 = np.polynomial.Polynomial(poly21)
print(poly21)
print(check_definition(poly21))
print(check_Hurwitz(poly21))
print(check_Routh(poly21))
