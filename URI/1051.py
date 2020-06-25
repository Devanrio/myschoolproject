a = float(input())

if a > 0.00 and a <= 2000 :
	print("Isento")
elif a > 2000 and a <= 3000 :
	b = 8/100
	c = (a - 2000)*b
	print("R$ %.2f"% c)
elif a > 3000 and a <= 4500 :
	b = 8/100
	c = 18 / 100
	d = (1000*b)+((a - 3000)*c)
	print("R$ %.2f"% d)
elif a > 4500 :
	b = 8/100
	c = 18 / 100
	d = 28 / 100
	e = (1000*b)+(1500*c)+((a - 4500)*d)
	print("R$ %.2f"% e)