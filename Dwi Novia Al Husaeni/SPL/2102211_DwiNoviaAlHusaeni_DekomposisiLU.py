import numpy as np
def lu_decomp(A):

    n = A.shape[0]
    if n == 1:
        L = np.array([[1]])
        U = A.copy()
        return (L, U)

    A11 = A[0,0]
    A12 = A[0,1:]
    A21 = A[1:,0]
    A22 = A[1:,1:]

    L11 = 1
    U11 = A11

    L12 = np.zeros(n-1)
    U12 = A12.copy()

    L21 = A21.copy() / U11
    U21 = np.zeros(n-1)

    S22 = A22 - np.outer(L21, U12)
    (L22, U22) = lu_decomp(S22)

    L = np.block([[L11, L12], [L21, L22]])
    U = np.block([[U11, U12], [U21, U22]])
    return (L, U)