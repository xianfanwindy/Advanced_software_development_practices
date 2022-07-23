#t1q4.py
while True:
    result = list(map(int,input().split()))
    if result[0]==0:
        break
    else:
        print(sum(result[1:]))
