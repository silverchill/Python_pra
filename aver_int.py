# average of a set of integers

total_num = int(input("Given intergers: "))

initial = 0
sum = 0

for initial in range(total_num):
    given = int(input("Enter your number: "))
    sum += given
    average = sum / total_num

print(average)
