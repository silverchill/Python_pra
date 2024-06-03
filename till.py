#  print the numbers from a given number n till 0 using recursion

def print_till_zero(num):
    print(num)
    
    if num <= 0:
        return 0
        
    print_till_zero(num - 1)
num = int(input("The given n value: "))

print_till_zero(num)
