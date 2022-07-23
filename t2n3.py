def min_difference(data):
    lists = []
    data.sort()
    
    for i in range(len(data)-1):
        lists.append(data[i+1]-data[i])
        
    result = min(lists)
    return result

n = input()
array = list(map(int,input().split()))
print(min_difference(array))
