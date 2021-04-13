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

print("X\tY\tOR_X\tOR_Y\tNR_X\tNR_Y")
for i in range(n):
	print("{}\t{}\t{}\t{}\t{}\t{}".format(X[i], Y[i], ranksX[i][0], ranksY[i][0], ranksX[i][1], ranksY[i][1]))

print(totalCorrectionFactor)