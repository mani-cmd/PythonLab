# John a software developer,
# Analyze a squence of numbers within a given range.
# Caclulate their digit sum
	# Exclude all palindrome numbers

X = input()
Y = input()
x = int(X)
y = int(Y)
sum = 0
for i in range(x, y+1):
	if not str(i) == str(i)[::-1]:
                j = i
                while(j!=0):
                    sum += j%10
                    j //= 10
print(sum)