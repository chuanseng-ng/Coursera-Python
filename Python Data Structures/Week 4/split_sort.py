fname = input("Enter file name: ")
fh = open(fname)
lst = list()                        # list() initializes lst as a list
for line in fh:
    stripped_line = line.split()    # split() splits up all the words separated by whitespaces in string into individual items
    for item in stripped_line:
        if item not in lst:         # item not in lst checks if item is not in lst and return true if valid
            lst.append(item)        # lst.append() pushes in item to the end of the list

lst.sort()                          # lst.sort() sorts all items in lst by alphabetical order

print(lst)
