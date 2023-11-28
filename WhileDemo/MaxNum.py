num_of_no = int(input("How Many Number you want to calculate: "))


count = 0
max = int(input('Enter a num'))

while count < num_of_no - 1:
    n = int(input("Enter a number: "))
    if n > max:
        max = n
    count += 1

print('Max num is ', max)

