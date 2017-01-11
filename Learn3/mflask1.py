# import win_unicode_console

import sys
from flask import Flask, request
import json
import requests

# win_unicode_console.enable()

def get_names_array(gender, born_year):
    t = requests.get("http://api.data.mos.ru/v1/datasets/" + str([2009, 2011][gender]) + "/rows")
    flist = json.loads(t.text)

    nlst = [dict(name=s.get('Cells').get('Name').replace('\n', ''), year=s.get('Cells').get('Year'),
				 month=s.get('Cells').get('Month'), num=s.get('Cells').get('NumberOfPersons')) 
    			for s in flist if s.get('Cells').get('Year') == born_year]

    nlst.sort(key=sort_by_name)
    names_dict = { d.get('name') : 0 for d in nlst}

    print(names_dict)
    
    # names_dict = list(set(names_dict))
    # names.sort()

    for d in nlst:
        names_dict[d.get("name")]+= d.get("num")
    
    return names_dict


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
    
    #for item in request.args:
    #	print(item)
    #	print(request.args.get(item))

    names_dict = get_names_array(0, 2015)
    html_str = '<table width="200" bgcolor="#c0c0c0" cellspacing="0" cellpadding="5" border="1" align="left"> <caption> Имена новорожденных девочек </caption>  <tr> <td> Имя </td> <td> Количество </td> </tr>'
    for n in names_dict.keys():
        html_str += '<tr> <td> ' + n + ' </td> <td>' + str(names_dict[n]) + '</td> </tr>'
    html_str += ' </table>'

    names_dict = get_names_array(1, 2015)
    html_str += '<table width="200" bgcolor="#c0c0c0" cellspacing="0" cellpadding="5" border="1" align="left"> <caption> Имена новорожденных мальчиков </caption>  <tr> <td> Имя </td> <td> Количество </td> </tr>'
    for n in names_dict.keys():
        html_str += '<tr> <td> ' + n + ' </td> <td>' + str(names_dict[n]) + '</td> </tr>'
    html_str += ' </table>'
    return html_str


if __name__ == "__main__" :

    app.run()
