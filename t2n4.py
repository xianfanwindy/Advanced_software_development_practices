n = int(input())
array1 = list(map(int,input().split()))
array2=sorted(array1)
minv = array2[1]-array2[0]
locf = 0
locb  =1 
for i in range(n-1):
    minva=array2[i+1]-array2[i]
    #locf=array1.index(array2[i])
    if(minv>minva):
        minv=minva
        locf=array1.index(array2[i])
        if minv==0:
            locb=array1.index(array2[i+1],(array1.index(array2[i])+1))
        else:
            locb=array1.index(array2[i+1])
print("{} {} {}".format(minv,locf+1,locb+1))
