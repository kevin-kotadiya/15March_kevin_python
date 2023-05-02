""" def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python')) """

string = ['kevin','kotadiya']

for n in string:
    print(n)
    if(len(n)) % 4 == 0:
        string[0],string[1] = string[1],string[0]
        
for s in string:
    print(s)
