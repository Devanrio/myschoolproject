N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
	a = int(N/nota)
	print("%i nota(s) de R$ %.2f" %(a, nota))
	N -= a*nota

print("MOEDAS:")
for moeda in moedas:
	a = int(round(N,2)/moeda)
	print("%i moeda(s) de R$ %.2f" %(a, moeda))
	N -= a*moeda