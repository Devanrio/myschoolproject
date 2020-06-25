X, Y = input().split()
X = int(X)
Y = int(Y)

price = {
	1 : 4.00,
	2 : 4.50,
	3 : 5.00,
	4 : 2.00,
	5 : 1.50
}

result = price[X]*Y

print("Total: R$ %.2f" %result)