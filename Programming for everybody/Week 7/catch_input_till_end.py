largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num_int = int(num)
        except:
            print("Invalid input")
    
    while largest is None:
        largest = num_int
    while smallest is None:
        smallest = num_int

    if largest < num_int:
        largest = num_int
    if smallest > num_int:
        smallest = num_int

print("Maximum is", largest)
print("Minimum is", smallest)