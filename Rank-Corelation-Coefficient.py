# Reading Input From File
file = open("input1.txt")
content = file.readlines()
file.close()

# Data X and Y
X = list(map(float, content[0].split(',')))
Y = list(map(float, content[1].split(',')))

# Total data
n = len(X)

# Calculating rank
def calculateRank(data):
	ranks = {x:i+1 for i,x in enumerate(sorted(list(set(data)), reverse=True))}
	return [ranks[i] for i in data]

# Calculating rank of X and Y
rankX = calculateRank(X)
rankY = calculateRank(Y)

# Finding absolute difference in ranks
d = [abs(rankX[i]-rankY[i]) for i in range(n)]
# Squares of absolute difference 
dSquare = list(map(lambda x: x * x, d))

# Calculating rank correlation coefficient
rankCorrelation = 1-((6*sum(dSquare))/(n*((n**2)-1)))

print()
print("n:", n)
print("X\tY\tRankX\tRankY\tD\tD^2")
for i in range(n):
	print("{}\t{}\t{}\t{}\t{}\t{}".format(X[i], Y[i], rankX[i], rankY[i], d[i], dSquare[i]))
print("ρ:", rankCorrelation)
print()