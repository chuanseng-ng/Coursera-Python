import urllib.request, urllib.parse, urllib.error
import json

sample = True
location = input("Enter location: ")
if len(location) < 1:
    sample_data = "http://py4e-data.dr-chuck.net/comments_42.json"
    actual_data = "http://py4e-data.dr-chuck.net/comments_1273230.json"
    if sample is True:
        location = sample_data
    else:
        location = actual_data

print("Retrieving ", location)
uh = urllib.request.urlopen(location)
data = uh.read().decode()
print ("Retrieved ", len(data), "characters")

try:
    info = json.loads(data)
except:
    info = None

total = 0
count = 0
for item in info["comments"]:
    total += int(item["count"])
    count += 1

print("Count: ", count)
print("Sum: ", total)