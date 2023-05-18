def runner(n,l):
    list1=list(set(l))
    list1.sort()
    return list1[-1]
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))



print(runner(n,l))
