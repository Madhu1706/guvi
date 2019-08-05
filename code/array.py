n,p=map(int,input().split())
m=list(map(int,input().split()))
count=0
for i in range(len(m)):
  for j in range(i+1,len(m)):
    if(m[i]+m[j]==p):
        count=1
        break
if(count):
   print("YES")
else:
   print("NO")
