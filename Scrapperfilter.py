import requests
import urllib.request,urllib.parse,urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
API_KEY = '52ebc366144a846306f837a876d21dda'
URL_TO_SCRAPE= url
payload = {'api_key':API_KEY,'url':URL_TO_SCRAPE}
r=requests.get('http://api.scraperapi.com',params=payload,timeout=60)
if r.status_code == 200:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    inpt = input('Enter the tag')
    t = inpt.split()
    #print(t[0])
    tags = soup(t[0])
    print("Want to get the pure text or source code?")
    which=input('If text press:1 else press:0')
    which = int(which)
if len(tags)>=0:
    for tag in tags:
        if which==1:
            print(tag.text)
        else:
            print(tag)
else:
    print("Error")
