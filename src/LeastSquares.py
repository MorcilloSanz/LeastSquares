"""
    Given the points: a1 = (a1x, a1y), a2 = (a2x, a2y), ..., ak = (akx, aky)
    Being k the number of points and n the order of the function we want to fit

    The function we're talking about is y = u1*x + u2*x^2 + ... + un*x^n. Its matrix form:
    

    ⎛       2        n⎞
    ⎜a1x a1x  ... a1x ⎟
    ⎜                 ⎟   ⎛u1⎞   ⎛a1y⎞
    ⎜       2        n⎟   ⎜  ⎟   ⎜   ⎟
    ⎜a2x a2x  ... a2x ⎟   ⎜u2⎟   ⎜a2y⎟
    ⎜                 ⎟   ⎜  ⎟ = ⎜   ⎟
    ⎜.   .    .   .   ⎟   ⎜. ⎟   ⎜.  ⎟
    ⎜                 ⎟   ⎜  ⎟   ⎜   ⎟
    ⎜       2        n⎟   ⎝un⎠   ⎝aky⎠
    ⎝akx akx  ... akx ⎠

    Being u1, u2, ..., un the solutions of the linear system

    There is no solution for: Ax = b (Which mean that not all the points are in the colspace)
    Multiplying both sides by A^T (A transpose):
        A^TAx = A^Tb

    Solving that new linear system we get the u1, u2, ..., un values which make the function
    'y' fit better with the points a1, a2, ..., ak

    If the residual 'ri', is ri = yi - y(xi), the function 'y' is the one which minimizes the
    sum:

      n
     ___
     ╲      2
     ╱    ri
     ‾‾‾
    i = 1
"""

import numpy as np

class LeastSquares:

    def __init__(self, points, order):
        # Input Data
        self.points = points
        self.order = order
        # Matrices
        self.A = None
        self.AT = None
        self.B = None
        # Solutions
        self.X = None
        # Calculate Least Squares
        self.__calculate()

    def __calculateA(self):
        a = []
        for i in range(0, len(self.points)):
            row = []
            for j in range(1, self.order + 1):
                row.append(pow(self.points[i][0], j))
            a.append(row)
        self.A = np.array(a)

    def __calculateB(self):
        b = []
        for i in range(0, len(self.points)):
            b.append(self.points[i][1])
        self.B = np.array(b)

    def __solveSystem(self):
        self.AT = np.transpose(self.A)
        ATA = np.matmul(self.AT, self.A)
        ATB = np.matmul(self.AT, self.B)
        self.X = np.linalg.solve(ATA, ATB)

    def __calculate(self):
        self.__calculateA()
        self.__calculateB()
        self.__solveSystem()

    def evaluateFunction(self, x):
        y = 0
        for i in range(0, self.order):
            y += self.X[i] * pow(x, i + 1)
        return y
