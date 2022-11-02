# s = "🐕💩🐕💩🐕💩🐕💩🐕💩🐕🐕🐕🐕💩💩💩💩💩💩"
#
# dic = {}
# for char in s:
#     if char not in dic:
#         dic[char] = 1
#     else:
#         dic[char] += 1  # 计数器
# print(dic)   # {'🐕': 9, '💩': 11}


from collections import Counter     # 这个效率快

s = "🐕💩🐕💩🐕💩🐕💩🐕💩🐕🐕🐕🐕💩💩💩💩💩💩"
c = Counter(s)  # 这个方法也能统计
print(c)  # Counter({'💩': 11, '🐕': 9})

for k, v in c.items():
    print(k,v)

