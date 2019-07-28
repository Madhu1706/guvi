n=int(input())
a=list(map(int,input().split(" ")))
s={}
for key in a:
    d[key]=a.count(key)

l=[]
for key,values in s.items():
    if(s[key]==1):
        print(key)
        break
