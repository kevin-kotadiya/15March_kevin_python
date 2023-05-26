def num(lists):
    ls = []

    for n in lists:
        ls.append(n)
    # print(ls) 
    m = max(ls)
    mi = min(ls)
    su = sum(ls)
    print(ls)
    print('max:',m)
    print('min:',mi)
    print('sum:',su)

# num([10,11,12,15,23,235,2323])
a = int(input("Enter number of elements:"))
l = []
for i in range(a):
    b = int(input("Enter mamber:"))
    l.append(b)

num(l)