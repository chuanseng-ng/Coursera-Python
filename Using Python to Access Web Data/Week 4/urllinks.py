# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

sample_input = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
actual_input = "http://py4e-data.dr-chuck.net/known_by_Patsy.html"

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1:
#    url = sample_input
    url = actual_input

count = int(input('Enter count: '))
position = int(input('Enter position: '))
new_count = 0
position_new = position - 1

# if new_count <= count, print current url and find 3rd url in page and go into found url and repeat
while(new_count <= count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving: ', url)
    url = tags[position_new].get('href', None)
    new_count += 1
