real = set([1,2,3,4,5,6])
bonus = 7
pick = set([1,2,3,4,5,7])

match_count = len(real.intersection(pick))

if match_count == 6:
    print(1)

elif match_count == 5 and bonus in pick:
    print(2)

elif match_count == 4:
    print(3)

elif match_count == 3:
    print(4)

elif match_count == 2:
    print(5)

