#t1q6.py
while True:
    result = list(map(int,input().split()))
    if result[0] == 0:
        break
    else:
        print(sum(result))
