def cube(x):
    s = x*x*x
    def square(x):
        s = x*x
        print("The square of s: ",s)
    g = int(input("The number to be squared: "))
    square(g)

    print("The cube of s: ",s)
h = int(input("The number to be cubed: "))
cube(h)
    