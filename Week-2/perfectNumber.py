# A perfect number is a number that equals the sum of its proper divisors (excluding itself)
# He wants to identify all perfect numbers within a range

n1 = int(input())
n2 = int(input())
# list1 = []
sum = 0
for i in range(n1, n2+1):
    for x in range(1, i):
        if i%x == 0:
            sum+=x
    if sum == i:
        print(i, end=" ")
    sum = 0

""" using while loop"""
# A perfect number is a number that equals the sum of its proper divisors (excluding itself)
# He wants to identify all perfect numbers within a range

n1 = int(input())
n2 = int(input())
# list1 = []
sum1 = 0
# for i in range(n1, n2+1):
i = n1
while i<=n2: 
    # for x in range(1, i):
    j = 1
    while j<i :
        if i%j == 0:
            sum1+=j
        j+=1
    if sum1 == i:
        print(i, end=" ")
    i+=1
    sum1 = 0
