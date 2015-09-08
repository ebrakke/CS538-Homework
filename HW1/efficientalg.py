cache = dict()
def efficient_alg(a, b, c):
	if b == 0:
		cache[b] = 0
		return 0
	if b == 1:
		if cache.get(b): return cache[b]
		cache[b] = a % c
		return cache[b]
	else:
		if cache.get(b): return cache[b]
		if b % 2 == 0:
			cache[b] = (efficient_alg(a, b/2, c) * efficient_alg(a, b/2, c)) % c
			return cache[b]
		else:
			cache[b] = (a * efficient_alg(a, b - 1, c)) % c
			return cache[b]
efficient_alg(7,100000000000,19)

# for i in range(1, 10000):
	# try:
	# 	assert pow(7, i, 19) == efficient_alg(7, i, 19)
	# except AssertionError as e:
	# 	print i, "Failed"
	# 	break
