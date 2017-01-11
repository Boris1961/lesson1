import json
import requests


t = requests.get("http://api.data.mos.ru/v1/datasets?$skip=1&$top=1&$inlinecount=allpages")
flist = json.loads(t.text)

print(flist)
