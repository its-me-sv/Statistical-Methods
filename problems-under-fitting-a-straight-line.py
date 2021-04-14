from tabulate import tabulate
from sympy import symbols, Eq, solve
from time import time

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
table.append(["Sigma(x)", "Sigma(Y)", "Sigma(x^2)", "Sigma(xy)"])
table.append([sigma_x, sigma_y, sigma_xSquare, sigma_xy])

# print(tabulate(table))

# print("normal equations are,")
eq1 = "{}a + ({})b = {}".format(sigma_x, n, sigma_y)
eq2 = "{}a + ({})b = {}".format(sigma_xSquare, sigma_x, sigma_xy)
# print(eq1, eq2, sep = '\n')
a, b, e = sigma_x, n, sigma_y
c, d, f = sigma_xSquare, sigma_x, sigma_xy
det = (a * d) - (b * c)

solvedA = ((e * d) - (b * f)) / det
solvedB = ((a * f) - (e * c)) / det

# print("Best fitting straight line,")
# print("y = {}x + ({})".format(solvedA, solvedB))

def prettyWriting():
	start = time()
	file = open("output3.txt", 'w')

	file.write("Let the straight line be y = ax + b\n")
	file.write("\nWeight of data,\n\tn = {}\n".format(n))

	file.write("\nThe normal equations to fit a straight line y = ax + b,\n")
	file.write("by means of method of least squares is,\n")
	file.write("\t\ta*Sigma(x) + n*b = Sigma(y)\n")
	file.write("\t\ta*Sigma(x^2) + b*Sigma(x) = Sigma(xy)\n")

	file.write("\nTherefore, the normal equations are,\n")
	file.write("\t\ta*Sigma(x) + {}*b = Sigma(y)\n".format(n))
	file.write("\t\ta*Sigma(x^2) + b*Sigma(x) = Sigma(xy)\n")

	file.write("\nFinding Sigma(x), Sigma(x^2), Sigma(y) and Sigma(xy),\n")
	file.write(tabulate(table)+"\n")

	file.write("\nTherefore, the normal equations are,\n")
	file.write("\t\t{}*a + {}*b = {} => (1)\n".format(sigma_x, n, sigma_y))
	file.write("\t\t{}*a + {}*b = {} => (2)\n".format(sigma_xSquare, sigma_x, sigma_xy))

	file.write("\nSolving Equations (1) and (2) by Cramer's rule,\n")
	file.write("\t\tD = [{}, {}]\n".format(a, b))
	file.write("\t\t    [{}, {}]\n".format(c, d))
	file.write("\t\tDx = [{}, {}]\n".format(e, b))
	file.write("\t\t     [{}, {}]\n".format(f, d))
	file.write("\t\tDy = [{}, {}]\n".format(a, e))
	file.write("\t\t     [{}, {}]\n".format(c, f))
	file.write("\t\ta = Det(Dx)/Det(D)\n")
	file.write("\t\t  = {}/{}\n".format((e * d) - (b * f), det))
	file.write("\t\t  = {}\n".format(solvedA))
	file.write("\t\tb = Det(Dy)/Det(D)\n")
	file.write("\t\t  = {}/{}\n".format((a * f) - (e * c), det))
	file.write("\t\t  = {}\n".format(solvedB))

	file.write("\nThus, the required equation,\n")
	file.write("\ty = ax + b\n")
	file.write("\ty = {}x + ({})".format(solvedA, solvedB))

	file.close()
	print("Solution Computed in {} second(s)".format(time()-start))

prettyWriting()