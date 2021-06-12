import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sample = False

url = input("Enter XML url: ")
if len(url) < 1:
    sample_data = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    actual_data = 'http://py4e-data.dr-chuck.net/comments_1273229.xml'
    if sample is True:
        url = sample_data
    else:
        url = actual_data

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved', len(uh), 'characters')
#print(uh.decode())
tree = ET.fromstring(uh)

lst = tree.findall('comments/comment')
for item in lst:
    count = int(item.find('count').text)
    total += count

print(total)
