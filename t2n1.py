c,n = input().split()
n = int(n)
for i in range(1,n+1):
    if i == 1:
        print(' ' * (n-i) + c)
    elif i == n:
        print(' ' * (n-i) + c +(' ' + c)*(i-1))
    else:
        print(' ' * (n-i) + c + ' ' * (2*(i-1)-1) +c)
