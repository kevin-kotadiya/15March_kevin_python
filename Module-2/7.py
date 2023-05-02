def tempdata(x,y,z):
    if x == y or x == z or y == z:
        sum = 0
    else:
        sum = x+y+z
        
    return sum
    
print(tempdata(2,1,2))
print(tempdata(3,2,2))
print(tempdata(2,2,2))
print(tempdata(1,1,1))
print(tempdata(1,2,3))