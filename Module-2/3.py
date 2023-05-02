Value = int(input("Enter any value:"))
n1,n2 = 0,1
i = 0

# for i in range(Value):
    
if Value == 0:
        print("Please enter positive interger value:")
elif Value < 0:
       print("nagative value not supported")
else:
        # print("fibonacci sequence:")
    for i in range(Value):
            print(n1)
            nth = n1+n2
            n1 = n2
            n2 = nth
            i+=1
    # print(final,)

    """ 
     0,1,1,2,3,5,8,13
       """