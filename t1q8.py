#t1q8
t=int(input())
for i in range(t):
    result = list(map(int,input().split()))
    print(sum(result[1:]))
    if (i+1)<t:
        print()
