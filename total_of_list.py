from itertools import combinations
list_ = [7,8,3,4,5,6]
target = 13
result = []
for i in range(1,len(list_)):
    bb = combinations(list_,i)
    for i in bb:
        if sum(i) == target:
            result.append(i)
print(result)