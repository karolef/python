#kata: https://www.codewars.com/kata/58df8b4d010a9456140000c7/train/python

def palindrome(num):

    hodl = []
    str_num = str(num)
    counter = 0
    up = down = num
    
    # checking if int and other conditions are met if not then not valid
    if isinstance(num,int) and num >= 0:
        # if single digit then always return 11
        if num < 10:
            return 11
        # if initial is palindrome return itself
        if str_num == str_num[::-1]:
            return num
        
        # find the closest lower palindrome
        while down >= 10:
            str_down = str(down)
            if str_down == str_down[::-1]:
                hodl.append(down)
                break
            down-=1
            
        # find the closest higher palindrome
        while True:
            str_up = str(up)
            if str_up == str_up[::-1]:
                hodl.append(up)
                break
            up+=1
        
        #return closer palindrome, if equal return higher
        if num - hodl[0] > hodl[1] - num:
            return hodl[1]
        elif num - hodl[0] < hodl[1] - num:
            return hodl[0]
        elif num - hodl[0] == hodl[1] - num:
            return hodl[1] 
        
        
    else:
        return "Not valid
