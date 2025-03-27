# # count non fibo numbs within a range, using continue
def findN(num):
    # if(num==0):
    #     return True
    t1=0
    t2=1
    t3=0
    while(t3<num):
        temp=t2
        t2,t3=t3,t2+t3
        t1=temp
    if(t3==num):
        return True
    else:
        return False


s = int(input())
e = int(input())
tot=0
for i in range(s, e+1):
    if(not(findN(i))):
        tot+=1

print(tot)
