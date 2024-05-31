# To check for even number

def is_even(number):
    return (number % 2 == 0)

# Test the function
Test_num = [4, 7, 6, -5, -9]

for number in Test_num:

    if is_even(number):
        print(f"{number} It's an even number")
    else:
        print(f"{number} It's an odd number")
