a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
counter = 0

angkas = [a,b,c,d,e,f,]

for angka in angkas:
	if angka < 0 :
		counter += 1

print("%i valores positivos"%counter)