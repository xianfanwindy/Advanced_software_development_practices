def max_difference(data):
    return max(data)-min(data)
n = int(input())
array = list(map(int,input().split()))
print(max_difference(array))
