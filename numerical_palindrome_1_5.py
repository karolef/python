# kata: https://www.codewars.com/kata/58e09234ca6895c7b300008c/train/python

def palindrome(num,s):
    hodl = []
    str_num = str(num)
    counter = 0

    # checking if int and other conditions are met if not then not valid
    if isinstance(num,int) and isinstance(s, int) and num >= 0 and s >= 0:
        # if s is 0 the hodl will always be empty
        if s == 0:
            return hodl
        # in this kata singletons are not palindromes
        elif num <= 10:
            num = 10
        # checking if initial num is palindrome
        elif str_num == str_num[::-1]:
            hodl.append(num)
            counter +=1 
            
        # checking numbers after given for palindromes till we have s of them
        while counter < s:
            num+=1
            str_num = str(num)
            if str_num == str_num[::-1]:
                hodl.append(num)
                counter +=1 

        return hodl
        
    else:
        return "Not valid"
