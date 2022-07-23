#t2n5.py
while True:
    data_hex = list(map(lambda x:int(x,16),input().split()))
    #data_dex = [int(x,16) for x in data_hex]
    print(sum(data_hex))
