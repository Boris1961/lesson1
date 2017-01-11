import requests
import html2text

R = requests.get("https://www.facebook.com")
S = html2text.HTML2Text(R)
print(type(S))
