def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

output_array = []
test_case = input()
for i in xrange(0,test_case):
	n = input()
	factors_n = prime_factors(n)
	count = 0
	for factor in factors_n:
		if factor == 3 or factor == 5:
			count += 1
	output_array.append(count)
for element in output_array:
	print element
