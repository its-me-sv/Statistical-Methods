def findNear(arr, target):
	if target in arr:
		return target
	cache = arr[:]
	cache = [[i, abs(i-target)] for i in arr]
	cache.sort(key = lambda x: x[1])
	return cache[0][0]