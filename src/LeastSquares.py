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