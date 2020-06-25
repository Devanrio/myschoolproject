a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

A = [a,b,c]
A.sort()

if A[2] >= A[0] + A[1]:
	print("NAO FORMA TRIANGULO")
elif A[2] == A[0] == A[1]:
	print("TRIANGULO ACUTANGULO")
	print("TRIANGULO EQUILATERO")
elif A[2] > A[0] and A[0] == A[1]:
	if A[2]**2 == A[0]**2 + A[1]**2:
		print("TRIANGULO RETANGULO")
		print("TRIANGULO ISOSCELES")
	elif A[2]**2 > A[0]**2 + A[1]**2:
		print("TRIANGULO OBTUSANGULO")
		print("TRIANGULO ISOSCELES")
	elif A[2]**2 < A[0]**2 + A[1]**2:
		print("TRIANGULO ACUTANGULO")
		print("TRIANGULO ISOSCELES")
elif A[2] > A[0] and A[1] == A[2]:
	if A[2]**2 == A[0]**2 + A[1]**2:
		print("TRIANGULO RETANGULO")
		print("TRIANGULO ISOSCELES")
	elif A[2]**2 > A[0]**2 + A[1]**2:
		print("TRIANGULO OBTUSANGULO")
		print("TRIANGULO ISOSCELES")
	elif A[2]**2 < A[0]**2 + A[1]**2:
		print("TRIANGULO ACUTANGULO")
		print("TRIANGULO ISOSCELES")
elif A[2] != A[0] and A[1] != A[2] and A[2] != A[1]:
	if A[2]**2 == A[0]**2 + A[1]**2:
		print("TRIANGULO RETANGULO")
	elif A[2]**2 > A[0]**2 + A[1]**2:
		print("TRIANGULO OBTUSANGULO")
	elif A[2]**2 < A[0]**2 + A[1]**2:
		print("TRIANGULO ACUTANGULO")