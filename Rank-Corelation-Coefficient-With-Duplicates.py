from tabulate import tabulate
from time import time

# Reading Input From File
file = open("input2.txt")
content = file.readlines()
file.close()

# Data X and Y
X = list(map(float, content[0].split(',')))
Y = list(map(float, content[1].split(',')))

# Total data
n = len(X)

def calculateRank(data):
	sortedData = sorted(data, reverse=True)
	cache = {}
	cf = 0
	for no in set(data):
		cache[no] = {}
		cache[no]["count"] = cnt = data.count(no)
		cache[no]["oldRank"] = oldRank = sortedData.index(no) + 1
		cache[no]["newRank"] = sum(range(oldRank, oldRank + cnt))/cnt
		cf += ((cnt**3)-cnt)/12
	rankObtained = [[cache[no]["oldRank"], cache[no]["newRank"]] for no in data]
	return {"ranks": rankObtained, "cf": cf}

specificationX = calculateRank(X)
ranksX = specificationX["ranks"]
specificationY = calculateRank(Y)
ranksY = specificationY["ranks"]

totalCorrectionFactor = specificationX["cf"] + specificationY["cf"]

table = [["X", "Y", "Old Rank X", "Old Rank Y", "New Rank X", "New Rank Y", "D", "D^2"]]
for i in range(n):
	d = abs(ranksX[i][1]-ranksY[i][1])
	dSquare = d * d
	table.append([X[i], Y[i], ranksX[i][0], ranksY[i][0], ranksX[i][1], ranksY[i][1], d, dSquare])

# print(tabulate(table))
# print(totalCorrectionFactor)
dSquareSum = sum([row[-1] for row in table[1:]]) +totalCorrectionFactor
rankCorrelation = 1-((6*dSquareSum))/(n*((n**2)-1))
# print(rankCorrelation)
# print("No correlation" if not rankCorrelation else "negative correlation" if rankCorrelation < 0.0 else "positive correlation")

def prettyWriting():
	file = open("output2.txt", 'w')
	start = time()
	file.write("Weight of data,\n\tn = {}\n".format(n))

	file.close()
	print("Solution computed in {} second(s)".format(time()-start))

prettyWriting()