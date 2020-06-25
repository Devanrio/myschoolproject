word, day1 = input().split()
line1 = input()
line1 = line1.replace(":", " ")
h1, m1, s1 = line1.split()
day1, h1, m1, s1 = int(day1), int(h1), int(m1), int(s1)
detik1 = (day1*24*3600) + (h1*3600) + (m1*60) + s1

word, day2 = input().split()
line2 = input()
line2 = line2.replace(":", " ")
h2, m2, s2 = line2.split()
day2, h2, m2, s2 = int(day2), int(h2), int(m2), int(s2)
detik2 = (day2*24*3600) + (h2*3600) + (m2*60) + s2

selisih = detik2 - detik1
selDay = selisih//(24*3600)
selisih -= selDay*24*3600

selHour = selisih//3600
selisih -= selHour*3600

selMinute = selisih//60
selisih -= selMinute*60

selDetik = selisih

print("%i dia(s)" % selDay)
print("%i hora(s)" % selHour)
print("%i minuto(s)" % selMinute)
print("%i segundo(s)" % selDetik)