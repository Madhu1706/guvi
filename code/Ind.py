n=int(input())
a=list(map(int,input().split(" ")))
l=[]
for i in range(len(a)):
    if(i==a[i]):
        l.append(i)
if l==[]:
   print("-1")
else:        
  l.sort()
  for i in l:
    print(i,end=" ")
