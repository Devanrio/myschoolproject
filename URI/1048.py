a = float(input())

if a > 0 and a <= 400.00 :
	b = 15/100
	c = a*(115/100)
	d = a*b
	print("Novo salario: %.2f"%c)
	print("Reajuste ganho: %.2f"%d)
	print("Em percentual: 15 %")
elif a > 400.00 and a <= 800.00 :
	b = 12/100
	c = a*(112/100)
	d = a*b
	print("Novo salario: %.2f"%c)
	print("Reajuste ganho: %.2f"%d)
	print("Em percentual: 12 %")
elif a > 800.00 and a <= 1200.00 :
	b = 10/100
	c = a*(110/100)
	d = a*b
	print("Novo salario: %.2f"%c)
	print("Reajuste ganho: %.2f"%d)
	print("Em percentual: 10 %")
elif a > 1200.00 and a <= 2000.00 :
	b = 7/100
	c = a*(107/100)
	d = a*b
	print("Novo salario: %.2f"%c)
	print("Reajuste ganho: %.2f"%d)
	print("Em percentual: 7 %")
if a > 2000.00 :
	b = 4/100
	c = a*(104/100)
	d = a*b
	print("Novo salario: %.2f"%c)
	print("Reajuste ganho: %.2f"%d)
	print("Em percentual: 4 %")