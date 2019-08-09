#Function
def LetterChanges(str): 
    str1 = []
    for x in str:
        str=chr(ord(x)+1).lower()
        if(str=='a' or str=='e' or str=='i' or str=='o' or str=='u'):
            str1.append(str.upper())
        else:
            str1.append(str)
    return (' '.join(str1))
    
#  Function call 
print LetterChanges(raw_input())  
