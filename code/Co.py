def longestCommonPrefix(word):
    longest_pre = ""
    if not word: return longest_pre
    shortest_word = min(word, key=len)
    for i in range(len(shortest_word)):
        if all([y.startswith(shortest_word[:i+1]) for y in word]):
            longest_pre = shortest_word[:i+1] 
        else:
            break 
    return longest_pre
s=int(input())
lst=[] 
for y in range(s):
        name=input()
        lst.append(name) 
op=longestCommonPrefix(lst)
if op=="":
    print("no")
else:
    print(op)





