n=int(input())
lst=[int(n) for n in input().split()]
a=0
for i in range(1,n+1):
    if(i*n in lst):
        a=a+1
print(a)
