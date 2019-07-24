n,p=map(int,input().split())
h=list(map(int,input().split()))
d=[]
for i in range(p):
    d.append(list(map(int,input().split())))
for i in d:
  su=0
  for j in range(i[0]-1,i[1]):
      su=su+m[h]
  print(su)
