a = int(input('Enter initial term'))
d = int(input('Enter common Difference'))
n = int(input('Enter Number of Terms'))
#here the logic is to get the max range we can do n*d + a
for t in range(a, a + n * d, d):
    print(t)