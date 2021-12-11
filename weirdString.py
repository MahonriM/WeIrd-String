def wird(string):
    new_string=''
    count=0
    for i in string:
        if i ==' ':
            new_string+=' '
            count=0
        else:
            if(count%2!=0):
                i=i
                new_string+=i
            elif(count%2==0):
                i=i.upper()
                new_string+=i
            count+=1
    return new_string
print(wird("String"))
#StRiNg 
