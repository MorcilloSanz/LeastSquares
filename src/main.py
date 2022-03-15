import matplotlib.pyplot as plt

from LeastSquares import LeastSquares

figure, axis = plt.subplots(2, 2)

# Points to fit
points = [
    (1, 5), (2, 8), (-1, -4),
    (3, 5), (-2, -2),(5, 8)
]

# -- Linear function --
leastSquares = LeastSquares(points, 1)

# plot function
x = range(-3, 7)  # x values
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


# -- Quadratic function --
leastSquares = LeastSquares(points, 2)

# plot function
x = range(-3, 7)  # x values
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


# -- Cubic function --
leastSquares = LeastSquares(points, 3)

# plot function
x = range(-3, 7)  # x values
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


# -- 4th order function --
leastSquares = LeastSquares(points, 4)

# plot function
x = range(-3, 7)  # x values
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