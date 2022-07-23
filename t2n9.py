n = int(input())
numList = list(set(map(int,input().split())))
numList.sort(reverse = True)
print(*numList)
