# factorial of a number using recursion

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        result = 1
        for n in range(2, n+1):
            result *= n
        return result
print(fact(4))

# Either of this two will give u a recussive factorial

def facti(m):
    if (m == 0 or m == 1):
        return 1
    else:
        return m * fact(m-1)
m = int(input("The given number: "))
print(facti(m))