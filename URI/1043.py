A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A > B and A > C and (B + C) > A:
	S = A + B + C
	print("Perimetro = %.1f"% S)
elif C > A and C > B and (A + B) > C:
	S = A + B + C
	print("Perimetro = %.1f"% S)
elif B > A and B > C and (A + C) > B:
	S = A + B + C
	print("Perimetro = %.1f"% S)
elif A == B and A == C:
	S = A + B + C
	print("Perimetro = %.1f"% S)
else:
	S = ((A+B)*C)/2
	print("Area = %.1f"% S)