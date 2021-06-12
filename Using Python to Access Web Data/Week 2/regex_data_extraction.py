import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1273225.txt"
#    name = "regex_sum_42.txt"
handle = open(name)
num_lst = list()

for line in handle:
    number = re.findall('[0-9]+', line)
    for item in number:
        num_lst.append(float(item))

sum = 0
for item in num_lst:
    sum += item

print(int(sum))