s=int(input())
sum=0
while(s!=0):
    rem=s%10
    sum=sum+(rem**2)
    s=int(s/10)
print(int(sum))
