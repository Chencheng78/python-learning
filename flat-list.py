# def flat_list(tree):
#     res = []
#     for i in tree:
#         if isinstance(i, list):
#             res.extend(flat_list(i))
#         else:
#             res.append(i)
#     return res
def flat_list(seq):
    s=str(seq).replace('[', '').replace(']', '')

    #return s.split(',')
    return [eval(x) for x in s.split(',') if x.strip()]

print(flat_list([[1], [2, [2], 2], [4]]))