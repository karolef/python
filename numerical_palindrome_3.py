# kata: https://www.codewars.com/kata/58df62fe95923f7a7f0000cc/train/python
# solved numerical palindrome 2 with almost the same code, just a slightly different output so posting only 3

def palindrome(num):
    

    str_num = str(num)
    palindromes = []

    # checking if input is correct
    if isinstance(num,int) and num >= 0:
        
        # looping over all of the strings in the input
        for i in range(len(str_num)):
            for j in range(0,i):
                sub_s = str_num[j:i+1]
                
                # checking if palindrome to append our list
                if sub_s == sub_s[::-1]:
                    palindromes.append(sub_s)
                    
        # return len of palindromes
        return len(palindromes)

    else:
        return "Not valid"
