#t1q7
flag = False
while True:
    result = list(map(int,input().split()))
    if flag:
        print()
    print(sum(result))
    flag =True
