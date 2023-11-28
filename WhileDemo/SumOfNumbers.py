num_of_no = int(input("How Many Number you want to calculate: "))


count = 0
psum = 0
nsum = 0

while count < num_of_no:
    n = int(input("Enter a number: "))
    if n > 0:
        psum = psum + n
    else:
        nsum = nsum + n
    count += 1

print('Positive Sum is ', psum)
print('Negative Sum is ', nsum)
