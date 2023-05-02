def ing(str):
    length = len(str)

    if length > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'

    return str
    
print(ing('ab'))
print(ing('abc'))
print(ing('eating'))