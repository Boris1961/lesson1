# /docs.python.org документация
# coding: utf-8
from collections import Counter
import csv

with open('data.csv', 'r', encoding='cp1251') as f:
	flist=csv.reader(f, delimiter=';')
	
	street_stat = [line[5] for line in flist]
	most_street = Counter(street_stat).most_common(10)
	print(most_street)
