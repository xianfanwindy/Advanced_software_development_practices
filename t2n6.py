#t2n6
while True:
    year,month,day = map(int, input().split("-"))
    print("{:0>2}/{:0>2}/{:0>4}".format(month,day,year))
