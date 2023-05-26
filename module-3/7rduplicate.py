
# Python code to remove duplicate elements
""" def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate)) """

a = [2,3,4,2,4,3,5,2,5,3,2,65,53,3,4,4,5,3,6,3,46,34,634,63,46,346,346]
final = []

for i in a:
    if i not in final:
        final.append(i)

print(final)