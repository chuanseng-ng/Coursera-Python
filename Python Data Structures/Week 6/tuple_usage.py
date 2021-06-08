name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hour = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        stripped_line = line.split()
        hour_only = stripped_line[5].split(":")
        hour[hour_only[0]] = hour.get(hour_only[0], 0) + 1      # New and faster method to replace below 4 lines

for keys,values in sorted(hour.items()):                        # sorted() sorts the dictionary key value pairs based on key before outputting
    print(keys, values)