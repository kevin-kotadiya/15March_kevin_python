def check(a,b):
    
    y = []

    for i in a:
        for j in b:
            if i == j:
                y.append(j)

    print(y)
    # if y > 0:
    #     print('True')
    # else:
    #     print('False')
    

check(['2','5','6','4'],['5','6','7','8'])