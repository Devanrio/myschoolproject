sh, sm, fh, fm = input().split()
sh = int(sh)
sm = int(sm)
fh = int(fh)
fm = int(fm)

if sh > fh and sm < fm :
	h = 24-(fh - sh)
	m = fm - sm
	print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (h,m))
elif sh > fh and sm > fm:
	h = (24-(sh - fh)) - 1
	m = 60 - (sm - fm)
	print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (h,m))
elif sh < fh and sm < fm :
	h = fh - sh
	m = fm - sm
	print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (h,m))
elif sh < fh and sm > fm :
	h = (fh - sh)-1
	m = 60 - (sm - fm)
	print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (h,m))
elif sh == fh and sm == fm :
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif sh == fh and sm > fm :
	m = 60 - (sm - fm)
	print("O JOGO DUROU 23 HORA(S) E %i MINUTO(S)" % (m))
elif sh == fh and sm < fm :
	m = fm - sm
	print("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" % (m))
elif sh > fh and sm == fm :
	h = 24 - (fh - sh)
	print("O JOGO DUROU %i HORA(S) E 0 MINUTO(S)" % (h))
elif sh < fh and sm == fm :
	h = fh - sh
	print("O JOGO DUROU %i HORA(S) E 0 MINUTO(S)" % (h))