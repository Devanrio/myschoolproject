A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
a = C + D
b = A + B
if B>C and D>A and a>b and C>0 and D>0 and A%2 == 0:
	print("Valores aceitos")
else:
	print("Valores nao aceitos")