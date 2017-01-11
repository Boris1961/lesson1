# import win_unicode_console
import sys
from flask import Flask, request
import json
import requests

# win_unicode_console.enable()

def sort_by_name(input_dict):
    return input_dict.get('name')

def sort_by_num(input_dict):
    return input_dict.get('num')

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/names"> Имена </a>'

@app.route("/names")
def nm():
    
    for item in request.args:
    	print(item)
    	print(request.args.get(item))

    html_str = '<table width="200" bgcolor="#c0c0c0" cellspacing="0" cellpadding="5" border="1" align="left"> <caption> Имена новорожденных девочек </caption>  <tr> <td> Имя </td> <td> Количество </td> </tr>'
    for n in names:
        html_str += '<tr> <td> ' + n + ' </td> <td>' + str(names_dict[n]) + '</td> </tr>'
    html_str += ' </table>'
    return html_str


if __name__ == "__main__" :

    t = requests.get("http://api.data.mos.ru/v1/datasets/2009/rows")
    flist = json.loads(t.text)

    nlst = [dict(name=s.get('Cells').get('Name').replace('\n', ''), year=s.get('Cells').get('Year'),
				 month=s.get('Cells').get('Month'), num=s.get('Cells').get('NumberOfPersons')) 
    			for s in flist if s.get('Cells').get('Year') == 2015]

    nlst.sort(key=sort_by_name)

    names = [d.get('name') for d in nlst]
    names = list(set(names))
    names.sort()

    names_dict = {n: 0 for n in names}

    for d in nlst:
        n = d.get("name")
        names_dict[n] += d.get("num")

    # print(names_dict)
    app.run()
