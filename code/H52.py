def steps(N):
    lst=[0,1,2]
    for i in range(3,N+1):
        sum=lst[i-1]+lst[i-2]
        lst.append(sum)
    return lst[N]
N=int(input())
y=steps(N)
print(y)
