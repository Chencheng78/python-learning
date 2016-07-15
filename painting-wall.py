'''
def checkio(wall,painting):
	此算法在大数字的情况下不好用
	count = 0
	painted_wall = set()
	for i in painting:
		painted_wall = painted_wall | set([j for j in range(i[0],i[1]+1)])
		if len(painted_wall) >= wall:
			count +=1
			return  count
		else:
			count +=1
	return -1
	'''
def Merge(covered, NewCover):
    # merge new into list
    NeedMerge = False
    for i in covered:
        if NewCover[1] < i[0] or i[1] < NewCover[0]:
            continue
        else:
            NeedMerge = True
            break
    if NeedMerge:
        covered.remove(i)
        covered.append([min(i[0], NewCover[0]), max(i[1], NewCover[1])])
    else:
        covered.append(NewCover)

    # internal merge
    if len(covered) > 1:
        NeedMerge = False
        for i in range(len(covered) - 1):
            for j in range(i + 1, len(covered)):
                if (covered[j][1] < covered[i][0]
                        or covered[i][1] < covered[j][0]):
                    continue
                else:
                    NeedMerge = True
                    break
            if NeedMerge:
                break
        if NeedMerge:
            temp = [min(covered[i][0], covered[j][0]),
                    max(covered[i][1], covered[j][1])]
            del covered[j]
            del covered[i]
            covered.append(temp)
    return covered


def checkio(required, operations):
    covered = []
    for i in operations:
        covered = Merge(covered, i)
        if sum([j[1] + 1 - j[0] for j in covered]) >= required:
            return operations.index(i) + 1
    return -1

print(checkio(16, [[1,5], [11,15], [2,14], [21,25]]))