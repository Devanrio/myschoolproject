a, b = input().split()
a = int(a)
b = int(b)

if a > b:
	A = 24-(a-b)
	print("O JOGO DUROU %i HORA(S)"% A)
elif b > a:
	A = -(a-b)
	print("O JOGO DUROU %i HORA(S)"% A)
else:
	print("O JOGO DUROU 24 HORA(S)")