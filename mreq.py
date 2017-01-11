import requests
import html2text

R = requests.get("https://www.facebook.com")
S = htnl2text.HTNL2Text(R)
