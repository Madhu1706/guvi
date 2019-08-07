n=input()
print(n[0].upper(),end="")
for i in range(1,(len(n)+1):
    if(n[i]!=" "):
        print(n[i].lower(),end="")
    else:
        print(n[i])
        print(n[i+1].upper(),end="")
