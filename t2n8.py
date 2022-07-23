team = 1
while True:
    try:
        n,q = map(int,input().split())
        card = list(map(int, input().split()))
        search = list(map(int, input().split()))
        card.sort()
        print("Case #{}:".format(team))
        for i in search:
            if i in card:
                print("{} found at {}".format(i,card.index(i)+1))
            else:
                print("{} not found".format(i))
        team += 1
    except:
        break
