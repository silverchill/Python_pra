# area of a triangle whose sides are given

a = float(input("Length of side of A = "))
b = float(input("Length of side of B = "))
c = float(input("Length of side of C = "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("s = {}, area = {}".format(s, area))
