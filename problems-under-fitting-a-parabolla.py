from tabulate import tabulate

# Reading Files
file = open("input4.txt")
content = file.readlines()
file.close()

# x Data
x = list(map(float, content[0].split(',')))
# y Data
y = list(map(float, content[1].split(',')))

# Finding n
n = len(x)

sigma_x = sum(x)
sigma_y = sum(y)

# Finding x^2, x^3, x^4, xy and x^2*y
xSquare = list(map(lambda a: a ** 2, x))
xCube = list(map(lambda a: a ** 3, x))
xFour = list(map(lambda a: a ** 4, x))

xy = [x[i]*y[i] for i in range(n)]
xSquarey = [xSquare[i]*y[i] for i in range(n)]

sigma_xSquare = sum(xSquare)
sigma_xCube = sum(xCube)
sigma_xFour = sum(xFour)

sigma_xy = sum(xy)
sigma_xSquarey = sum(xSquarey)

table = [['x', 'y', 'x^2', 'x^3', 'x^4', 'xy', 'x^2*y']]

for i in range(n):
	table.append([x[i], y[i], xSquare[i], xCube[i], xFour[i], xy[i], xSquarey[i]])

table.append([sigma_x, sigma_y, sigma_xSquare, sigma_xCube, sigma_xFour, sigma_xy, sigma_xSquarey])

print(tabulate(table))

print("The normal equations are,")
eq1 = "({})a + ({})b + ({})c = {}".format(sigma_xSquare, sigma_x, n, sigma_y)
eq2 = "({})a + ({})b + ({})c = {}".format(sigma_xCube, sigma_xSquare, sigma_x, sigma_xy)
eq3 = "({})a + ({})b + ({})c = {}".format(sigma_xFour, sigma_xCube, sigma_xSquare, sigma_xSquarey)

print(eq1, eq2, eq3, sep = '\n')

a1, b1, c1, l = sigma_xSquare, sigma_x, n, sigma_y
a2, b2, c2, m = sigma_xCube, sigma_xSquare, sigma_x, sigma_xy
a3, b3, c3, n = sigma_xFour, sigma_xCube, sigma_xSquare, sigma_xSquarey

D = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]
Dx = [[l, b1, c1], [m, b2, c2], [n, b3, c3]]
Dy = [[a1, l, c1], [a2, m, c2], [a3, n, c3]]
Dz = [[a1, b1, l], [a2, b2, m], [a3, b3, n]]

def getDeterminant(mat):
	multiply = lambda a, b, c, d: (a * d) - (b * c)
	s1 = mat[0][0]*multiply(mat[1][1], mat[1][2], mat[2][1], mat[2][2])
	s2 = (-mat[0][1])*multiply(mat[1][0], mat[1][2], mat[2][0], mat[2][2])
	s3 = mat[0][2]*multiply(mat[1][0], mat[1][1], mat[2][0], mat[2][1])
	return s1 + s2 + s3

solvedA = getDeterminant(Dx)/getDeterminant(D)
solvedB = getDeterminant(Dy)/getDeterminant(D)
solvedC = getDeterminant(Dz)/getDeterminant(D)

print("Equation of parabola is,")
finalEquation = "y = ({})x^2 + ({})x + ({})".format(solvedA, solvedB, solvedC)
print(finalEquation)