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
dSquareSum = sum([row[-1] for row in table[1:]]) + totalCorrectionFactor
rankCorrelation = 1-((6*dSquareSum))/(n*((n**2)-1))
# print(rankCorrelation)
# print("No correlation" if not rankCorrelation else "negative correlation" if rankCorrelation < 0.0 else "positive correlation")

def duplicateFinder(dataset1):
	if len(set(dataset1)) == len(dataset1):
		return False
	completeDataset = dataset1[:]
	sortedCompleteDataset = sorted(completeDataset, reverse=True)
	cache = {}
	for no in set(completeDataset):
		if completeDataset.count(no) == 1:
			continue
		cache[no] = {}
		cache[no]["count"] = cnt = completeDataset.count(no)
		cache[no]["oldRank"] = oldRank = sortedCompleteDataset.index(no) + 1
		cache[no]["newRank"] = sum(range(oldRank, oldRank + cnt))/cnt
		cache[no]["cf"] = ((cnt**3)-cnt)/12
		cache[no]["rankCalculation"] = "({})/{}".format(" + ".join(list(map(str, range(oldRank, oldRank + cnt)))),cnt)
	return cache

def sortDuplicateData(dataset1, dataset2, fileObj):
	if len(set(dataset1)) == len(dataset1) and len(set(dataset2)) == len(dataset2):
		fileObj.write("\nNo Duplicate Data Found in X and Y\n")
		return
	resultX = duplicateFinder(dataset1)
	if not resultX:
		fileObj.write("\nNo Duplicate Data Found in X\n")
	else:
		fileObj.write("\nDuplicate Data Found in X,\n")
		tableX = [["Index", "Count", "Rank Calculation", "New Rank", "Correction Factor"]]
		for key in resultX:
			obtResult = resultX[key]
			tableX.append([key, obtResult["count"], obtResult["rankCalculation"], obtResult["newRank"], obtResult["cf"]])
		fileObj.write(tabulate(tableX)+"\n")

	resultY = duplicateFinder(dataset2)
	if not resultY:
		fileObj.write("\nNo Duplicate Data Found in Y\n")
	else:
		fileObj.write("\nDuplicate Data Found in Y,\n")
		tableY = [["Index", "Count", "Rank Calculation", "New Rank", "Correction Factor"]]
		for key in resultY:
			obtResult = resultY[key]
			tableY.append([key, obtResult["count"], obtResult["rankCalculation"], obtResult["newRank"], obtResult["cf"]])
		fileObj.write(tabulate(tableY)+"\n")
	fileObj.write("\n")

def prettyWriting():
	file = open("output2.txt", 'w')
	start = time()
	file.write("Weight of data,\n\tn = {}\n".format(n))

	temp = [["X", "Y", "Rank X", "Rank Y"]]
	for i in range(n):
		temp.append([X[i], Y[i], ranksX[i][0], ranksY[i][0]])

	file.write("\nFinding Rank of X and Y,\n")
	file.write(tabulate(temp)+"\n")

	sortDuplicateData(X, Y, file)

	file.write("Total Correction Factor(CF) = {}\n".format(totalCorrectionFactor))
	file.write("\nRequired Table, \n")
	file.write(tabulate(table)+"\n")

	file.write("\nSigma(D^2) = {}\n".format(" + ".join([str(row[-1]) for row in table[1:]])))
	file.write("            = {}\n".format(sum([row[-1] for row in table[1:]])))
	file.write("            = {} (After Adding Total Correction Factor(CF) of {})\n".format(dSquareSum, totalCorrectionFactor))

	file.write("\nFinding Spearman's Coefficient of rank correlation,\n")
	file.write("\tRho = 1 - (6*Sigma(D^2))/(n*((n^2)-1))\n")
	file.write("\t    = 1 - (6*{})/({}*(({}^2)-1))\n".format(dSquareSum, n, n))
	file.write("\t    = 1 - ({})/({})\n".format(6*dSquareSum, n*((n**2)-1)))
	file.write("\t    = 1 - {}\n".format(((6*dSquareSum))/(n*((n**2)-1))))
	file.write("\t    = {}\n".format(rankCorrelation))

	file.write("\n")
	theory = "No Correlation" if not rankCorrelation else "Negative Correlation" if rankCorrelation < 0.0 else "Positive Correlation"
	file.write("Thus, {} Between the given data\n".format(theory))

	file.close()
	print("Solution computed in {} second(s)".format(time()-start))

prettyWriting()