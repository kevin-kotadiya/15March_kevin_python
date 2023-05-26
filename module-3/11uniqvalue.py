def uniq_numbers(u):

    x = []

    for i in u:
        if i not in x:
            x.append(i)

    print(x)

uniq_numbers([1,2,4,2,2,2,3,33,4,2,2,3,34,2,23,44,5,5,5,5,3,2,2,3,4])