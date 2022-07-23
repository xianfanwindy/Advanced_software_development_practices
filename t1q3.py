#t1q3
while True:
    result = list(map(int,input().split()))
    if result == [0,0]:
        break
    else:
        print(sum(result))
