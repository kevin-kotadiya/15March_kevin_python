# def match_words(words):
#   ctr = 0

#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#     #   ctr += 1
#         print(word)
#   return ctr

# print(match_words(['abc', 'xyz', 'aba', '1221']))

a = ['abc','aba','cde','ard','12321']
b = []
for i in a:
    # print(a[0])
    if len(i) > 1 and i[0] == i[-1]:
        b.append(i)

print(b)
