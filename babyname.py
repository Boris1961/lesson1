# /docs.python.org документация
# coding: utf-8

# MOS.RU boris1961 pass=EAGLES261 key=14e1239edc198f0a560022553dcb45bf

from collections import Counter
import json
import requests


def sort_by_name(input_dict):
	return input_dict.get('name')

def sort_by_num(input_dict):
	return input_dict.get('num')


t = requests.get("http://api.data.mos.ru/v1/datasets/2009/rows")
flist = json.loads(t.text)



nlst = [ dict(name=s.get('Cells').get('Name').replace('\n',''), \
			  year=s.get('Cells').get('Year'), \
			  month=s.get('Cells').get('Month'), \
			  num=s.get('Cells').get('NumberOfPersons')) \
		 for s in flist if s.get('Cells').get('Year')==2015 ]


""""
for d in nlst:
	if d.get('name') == "Наталья":
		print(d)
"""

nlst.sort(key=sort_by_name)

names = [ d.get('name') for d in nlst ]
names = list(set(names))

names_dict = {n:0 for n in names }

for d in nlst:
	n = d.get("name")
	names_dict[n] += d.get("num")

names_dict = sorted(names_dict.items())

print(names_dict)

