N1, N2, N3, N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
A = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
if A >= 7.0:
	print("Media: %.1f" %A)
	print("Aluno aprovado.")
elif A < 5.0:
	print("Media: %.1f" %A)
	print("Aluno reprovado.")
else:
	N5 =  float(input())
	AB = (N5 + A)/2
	print("Media: %.1f" %A)
	print("Aluno em exame.")
	print("Nota do exame: %.1f" %N5)
	if AB >= 5.0:
		print("Aluno aprovado.")
		print("Media final: %.1f" %AB)
	else:
		print("Aluno reprovado.")
		print("Media final: %.1f" %AB)