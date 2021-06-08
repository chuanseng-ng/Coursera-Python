name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
spam = dict()                                                           # dict() initializes spam as a dictionary
lst = list()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        stripped_line = line.split()
        spam[stripped_line[1]] = spam.get(stripped_line[1], 0) + 1      # New and faster method to replace below 4 lines
#        if stripped_line[1] not in spam:
#            spam[stripped_line[1]] = 1                                 # Initialize dictionary key value as 1
#        else:
#            spam[stripped_line[1]] += 1                                # Increment dictionary key value by 1 if key is found again

maximum = None
spammer = None
for keys,values in spam.items():                                        # Shortcut to access both key and value in dictionary at the same time, require use of items()
    if maximum is None or values > maximum:
        maximum = values
        spammer = keys

print(spammer, maximum)