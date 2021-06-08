# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):  # startswith("test") checks if test is present in string
        count += 1
        x = line.find("0")                      # find("test") finds first iteration of keyword test in string and return position
        length = len(line)                      # len(variable) returns length of variable
        number = float(line[x:length])
        total += number

average = total / count
print("Average spam confidence:", average)   