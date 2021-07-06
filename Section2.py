def findSum(n):

	dp = [0 for i in range(n + 1)]

	dp[1] = 1
	dp[0] = 0

	for i in range(2, n + 1, 1):
		dp[i] = ((4 * (i * i)) - 6 *
					(i - 1) + dp[i - 2])

	return dp[n]

if __name__ == '__main__':
	n = 4

	print(findSum(n))
