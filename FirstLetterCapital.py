#Capitalize First letter function
def LetterCapitalize(str): 

    str1 = []
    x = str.split(" ")
    for i in x:
        str1.append(i[0].upper()+i[1:])
  
    return " ".join(str1)
    
# function call here  
print LetterCapitalize(raw_input()) 
