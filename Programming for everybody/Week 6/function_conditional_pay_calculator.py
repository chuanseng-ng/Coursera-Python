def computepay(h, r):
    if h <= 40:
        p = h * r
    else:
        p = 40 * r
        o = (h - 40) * (r * 1.5)
        p = p + o
    return p

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

h = float(hrs)
r = float(rate)

p = computepay(h, r)
print("Pay", p)