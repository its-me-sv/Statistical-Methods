from tabulate import tabulate
from sympy import symbols, Eq, solve

# Reading Data
file = open("input3.txt")
content = file.readlines()
file.close()

# x Data
x = list(map(float, content[0].split(',')))
# y Data
y = list(map(float, content[1].split(',')))

# Finding n
n = len(x)

# Finding X^2
xSquare = list(map(lambda a: a * a, x))
# Finding XY
xy = [x[i]*y[i] for i in range(n)]

# Finding Σx, Σy, Σx^2 and Σxy
sigma_x = sum(x)
sigma_y = sum(y)
sigma_xSquare = sum(xSquare)
sigma_xy = sum(xy)


# Making Table
table = [['x', 'y', 'x^2', 'xy']]
for i in range(n):
	table.append([x[i], y[i], xSquare[i], xy[i]])
table.append([sigma_x, sigma_y, sigma_xSquare, sigma_xy])

print(tabulate(table))

print("normal equations are,")
eq1 = "{}a + ({})b = {}".format(sigma_x, n, sigma_y)
eq2 = "{}a + ({})b = {}".format(sigma_xSquare, sigma_x, sigma_xy)
print(eq1, eq2, sep = '\n')
a, b, e = sigma_x, n, sigma_y
c, d, f = sigma_xSquare, sigma_x, sigma_xy
det = (a * d) - (b * c)

solvedA = ((e * d) - (b * f)) / det
solvedB = ((a * f) - (e * c)) / det

print("Best fitting straight line,")
print("y = {}x + ({})".format(solvedA, solvedB))