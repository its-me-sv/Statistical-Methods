from NearingPlace import findNear
from time import time
from tabulate import tabulate

def precisionOf3(ans):
	return round(ans, 3)

# Reading Input From File
file = open("input.txt")
content = file.readlines()
file.close()

# x Data
x = list(map(float, content[0].split(',')))
# y Data
y = list(map(float, content[1].split(',')))

# Total Elements
n = len(x)

# Mean of x and y Data
tempxBar = round(sum(x)/n, 2)
xBar = round(sum(x)/n)
xBar = findNear(x, xBar)
tempyBar = round(sum(y)/n, 2)
yBar = round(sum(y)/n)
yBar = findNear(y, yBar)


X = list(map(lambda v: precisionOf3(v - xBar), x))
Y = list(map(lambda v: precisionOf3(v - yBar), y))


XSquare = list(map(lambda a: precisionOf3(a*a), X))
YSquare = list(map(lambda a: precisionOf3(a*a), Y))


XY = [precisionOf3(i*j) for i, j in zip(X, Y)]

# Sums of X, Y, X^2, Y^2, XY
sigmaX = sum(X)
sigmaY = sum(Y)
sigmaXSquare = sum(XSquare)
sigmaYSquare = sum(YSquare)
sigmaXY = sum(XY)

# Mean of X and Y
XBar = precisionOf3(sum(X)/n)
YBar = precisionOf3(sum(Y)/n)

# σ of X and Y
siX = precisionOf3(((sigmaXSquare/n) - (XBar**2)) ** 0.5)
siY = precisionOf3(((sigmaYSquare/n) - (YBar**2)) ** 0.5)

# Covarience of X and Y
covXY = precisionOf3((sigmaXY/n) - (XBar*YBar))

# Coefficient of Correlation
coeffCovXY = precisionOf3(covXY/(siX*siY))

def lor(barValue1, r, nr, dr, barValue2, var):
	varPrefix = precisionOf3(r * (nr/dr))
	constant = (varPrefix * (-barValue2))+barValue1
	constant = precisionOf3(constant)
	return "{}{}{}".format(varPrefix, var, constant)

# Equation of lines of regression of y on x
lorYX = lor(yBar, coeffCovXY, siY, siX, xBar, 'x')
# Equation of lines of regression of x on y
lorXY = lor(xBar, coeffCovXY, siX, siY, yBar, 'y')

# print()
# print("n:", n)
# print("Mean(x):", xBar)
# print("Mean(y):", yBar)
# print("x\ty\tX\tY\tX^2\tY^2\tXY")
# for i in range(n):
# 	print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(x[i], y[i], X[i], Y[i], XSquare[i], YSquare[i], XY[i]))
# print("Σ(X):", sigmaX)
# print("Σ(Y):", sigmaY)
# print("Σ(X^2):", sigmaXSquare)
# print("Σ(Y^2):", sigmaYSquare)
# print("Σ(XY):", sigmaXY)
# print("Mean(X):", XBar)
# print("Mean(Y):", YBar)
# print("σ(X):", siX)
# print("σ(Y):", siY)
# print("Covarience(X,Y)", covXY)
# print("Coefficient of Correlation r(X,Y):", coeffCovXY)
# print("Equation of lines of regression of y on x:", lorYX)
# print("Equation of lines of regression of x on y:", lorXY)
# print()

def prettyWriting():
	file = open("output.txt", 'w')
	start = time()
	file.write("Weight of data,\n\tn = {}\n".format(n))
	
	file.write("\nFinding Mean(x) and Mean(y),\n")
	concater = lambda k: " + ".join(list(map(str, k)))
	file.write("\t\tMean(x) = sigma(x)/n = ({})/{} = {} (nearing no is {})\n".format(concater(x), n, tempxBar, xBar))
	file.write("\t\tMean(y) = sigma(y)/n = ({})/{} = {} (nearing no is {})\n".format(concater(y), n, tempyBar, yBar))
	file.write("\nTherefore,\n")
	file.write("\tMean(x) = {}\n".format(xBar))
	file.write("\tMean(y) = {}\n".format(yBar))
	
	file.write("\nFinding X, Y, X^2, Y^2 and XY,\n")
	file.write("\tX = x - Mean(x)\n")
	file.write("\t  = x - {}\n".format(xBar))
	file.write("\tY = y - Mean(y)\n")
	file.write("\t  = y - {}\n\n".format(yBar))
	
	table = [['x','y','X','Y','X^2','Y^2','XY']]
	for i in range(n):
		table.append([x[i], y[i], X[i], Y[i], XSquare[i], YSquare[i], XY[i]])
	table.append(["sigma(x)", "sigma(y)", "sigma(X)", "sigma(Y)", "sigma(X^2)", "sigma(Y^2)", "sigma(XY)"])
	table.append([sum(x), sum(y), sigmaX, sigmaY, sigmaXSquare, sigmaYSquare, sigmaXY])
	file.write(tabulate(table)+'\n')
	
	file.write("\nFinding Mean(X) and Mean(Y),\n")
	file.write("\t\tMean(X) = sigma(X)/n = {}/{} = {}\n".format(sigmaX, n, XBar))
	file.write("\t\tMean(Y) = sigma(Y)/n = {}/{} = {}\n".format(sigmaY, n, YBar))
	
	file.write("\nFinding si(X) and si(Y),\n")
	file.write("\t\tsi(X) = sqrt((sigma(X^2)/n)-(Mean(X)^2))\n")
	file.write("\t\t      = sqrt(({}/{})-({}))\n".format(sigmaXSquare, n, XBar))
	file.write("\t\t      = sqrt({})\n".format(round((sigmaXSquare/n)-(XBar**2), 3)))
	file.write("\t\t      = {}\n".format(siX))
	file.write("\t\tsi(Y) = sqrt((sigma(Y^2)/n)-(Mean(Y)^2))\n")
	file.write("\t\t      = sqrt(({}/{})-({}))\n".format(sigmaYSquare, n, YBar))
	file.write("\t\t      = sqrt({})\n".format(round((sigmaYSquare/n)-(YBar**2), 3)))
	file.write("\t\t      = {}\n".format(siY))
	
	file.write("\nFinding Covarience of X and Y,\n")
	file.write("\t\tCOV(X,Y) = (sigma(XY)/n) - (Mean(X)*Mean(Y))\n")
	file.write("\t\t         = ({}/{}) - ({}*{})\n".format(sigmaXY, n, XBar, YBar))
	file.write("\t\t         = {}\n".format(covXY))	
	
	file.write("\nFinding Coefficient of Covarience,\n")
	file.write("\t\tr(X,Y) = COV(X,Y) / (si(X)*si(Y))\n")
	file.write("\t\t       = {} / ({}*{})\n".format(covXY, siX, siY))
	file.write("\t\t       = {} / {}\n".format(covXY, round(siX*siY, 3)))
	file.write("\t\t       = {}\n".format(coeffCovXY))
	
	file.write("\nEquation of lines of regression of y on x,\n")
	file.write("\t\ty - Mean(y) = r * (si(Y)/si(X)) * (x - Mean(x))\n")
	file.write("\t\ty - {} = {} * ({}/{}) * (x - {})\n".format(yBar, coeffCovXY, siY, siX, xBar))
	file.write("\t\ty - {} = {} * {} * (x - {})\n".format(yBar, coeffCovXY, round(siY/siX, 3), xBar))
	file.write("\t\ty - {} = {} * (x - {})\n".format(yBar, round(coeffCovXY*round(siY/siX, 3), 3), xBar))
	cx = round(coeffCovXY*round(siY/siX, 3), 3)
	cc = round(cx * (-xBar), 3)
	file.write("\t\ty = {}x - ({}) + ({})\n".format(cx, cc, yBar))
	file.write("\t\ty = {}\n".format(lorYX))

	file.write("\nEquation of lines of regression of x on y,\n")
	file.write("\t\tx - Mean(x) = r * (si(X)/si(Y)) * (y - Mean(y))\n")
	file.write("\t\tx - {} = {} * ({}/{}) * (y - {})\n".format(xBar, coeffCovXY, siX, siY, yBar))
	file.write("\t\tx - {} = {} * {} * (y - {})\n".format(xBar, coeffCovXY, round(siX/siY, 3), yBar))
	file.write("\t\tx - {} = {} * (y - {})\n".format(xBar, round(coeffCovXY*round(siX/siY, 3), 3), yBar))
	cy = round(coeffCovXY*round(siX/siY, 3), 3)
	cc = round(cy * (-yBar), 3)
	file.write("\t\tx = {}y - ({}) + ({})\n".format(cy, cc, xBar))
	file.write("\t\ty = {}\n".format(lorXY))

	file.write("\nThus, we have found the Coefficient of Correlation and Lines of Regression for the given data.")

	file.close()
	print("Solution computed in {} second(s)".format(time()-start))

prettyWriting()