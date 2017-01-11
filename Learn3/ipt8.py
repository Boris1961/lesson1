y = int(input("Сколько лет:"))

a = 6000000
p = 0.11/12
m = y*12
s = 0
ost = a
for i in range (1,m):
	s += ost*p
	ost *= 1 - 1/m
print ("Переплата = ", s)
print ("Сумма = ", a+s, "/n Месяцев = ", m)
print ("Месячная плата = ", (a+s)/m)
