# kata: https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a/train/python
# top commented out code works for small test cases, but timed out for bigger ones because it checked all permutations of the list hence bottom fnc
'''
import itertools

def palindrome(num):
    str_num = str(num)
    
    if isinstance(num,int) and num >= 0:
        if num < 10:
            return False

        for subset in itertools.permutations(str_num, len(str_num)):
            if subset == subset[::-1]:
                return True
        
        return False
        
    else:
        return "Not valid"
'''

def palindrome(num):
    str_num = str(num)
    if isinstance(num,int) and num >= 0:
        return sum(map(lambda x: str_num.count(x) % 2, str_num)) <= 1 and num > 10
    else:
        return 'Not valid'
