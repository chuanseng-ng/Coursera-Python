# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line_s = line.rstrip()  # rstrip() removes trailing whitespaces in string
    print(line_s.upper())   # upper() changes all characters in string to uppercase, if applicable