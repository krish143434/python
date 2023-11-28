n = int(input("whats the number: "))

sum = 0

while n > 0:
    r = n % 10
    n = n // 10
    sum += r
print('Sum of Digits is', sum)