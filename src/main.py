import matplotlib.pyplot as plt

from LeastSquares import LeastSquares

figure, axis = plt.subplots(2, 2)

# -- Linear --
points = [(1, 5), (2, 8), (-1, -4), (3, 5), (-2, -2)]
leastSquares = LeastSquares(points, 1)

# plot function
x = range(-10, 10)  # x values
y = []
for i in x:
    y.append(leastSquares.evaluateFunction(i))

axis[0, 0].plot(x,y, 'b-')

# plot points
pointsx = []
for i in range(0, len(points)):
    pointsx.append(points[i][0])

pointsy = []
for i in range(0, len(points)):
    pointsy.append(points[i][1])

axis[0, 0].plot(pointsx, pointsy, 'ro')
axis[0, 0].set_title("Order: " + str(leastSquares.order))


# -- Quadratic --
points = [(1, 5), (2, 8), (-1, -4), (3, 5), (-2, -2)]
leastSquares = LeastSquares(points, 2)

# plot function
x = range(-10, 10)  # x values
y = []
for i in x:
    y.append(leastSquares.evaluateFunction(i))

axis[0, 1].plot(x,y, 'b-')

# plot points
pointsx = []
for i in range(0, len(points)):
    pointsx.append(points[i][0])

pointsy = []
for i in range(0, len(points)):
    pointsy.append(points[i][1])

axis[0, 1].plot(pointsx, pointsy, 'ro')
axis[0, 1].set_title("Order: " + str(leastSquares.order))


# -- Cubic  --
points = [(1, 5), (2, 8), (-1, -4), (3, 5), (-2, -2)]
leastSquares = LeastSquares(points, 3)

# plot function
x = range(-5, 5)  # x values
y = []
for i in x:
    y.append(leastSquares.evaluateFunction(i))

axis[1, 0].plot(x,y, 'b-')

# plot points
pointsx = []
for i in range(0, len(points)):
    pointsx.append(points[i][0])

pointsy = []
for i in range(0, len(points)):
    pointsy.append(points[i][1])

axis[1, 0].plot(pointsx, pointsy, 'ro')
axis[1, 0].set_title("Order: " + str(leastSquares.order))


# -- 4th order --
points = [(1, 5), (2, 8), (-1, -4), (3, 5), (-2, -2)]
leastSquares = LeastSquares(points, 4)

# plot function
x = range(-5, 5)  # x values
y = []
for i in x:
    y.append(leastSquares.evaluateFunction(i))

axis[1, 1].plot(x,y, 'b-')

# plot points
pointsx = []
for i in range(0, len(points)):
    pointsx.append(points[i][0])

pointsy = []
for i in range(0, len(points)):
    pointsy.append(points[i][1])

axis[1, 1].plot(pointsx, pointsy, 'ro')
axis[1, 1].set_title("Order: " + str(leastSquares.order))



plt.show()