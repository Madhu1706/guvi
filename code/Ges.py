n,r=map(int,input().split())
q=list(map(int,input().split()))
p=[]
for i in range(r):
    p.append(list(map(int,input().split())))
for i in p:
  su=0
  for j in range(i[0]-1,i[1]):
      su=su+q[j]
  print(su)
