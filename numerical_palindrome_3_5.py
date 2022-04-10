# kata: https://www.codewars.com/kata/58e2708f9bd67fee17000080/train/python

def palindrome(num):    

    str_num = str(num)
    palindromes = []

    # checking if input is correct
    if isinstance(num,int) and num >= 0:
        
        # looping over all of the strings in the input
        for i in range(len(str_num)):
            for j in range(0,i):
                sub_s = str_num[j:i+1]
                
                # checking if palindrome to append our list cannot start or end with 0
                if sub_s == sub_s[::-1] and sub_s[0] != '0' and sub_s[len(sub_s) - 1] != '0':
                    palindromes.append(int(sub_s))
                    
                    
        # return palindromes without duplicates & sorted
        if palindromes:
            return sorted(list(set(palindromes)))
        else:
            return "No palindromes found"

    else:
        return "Not valid"
