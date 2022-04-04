# codewars problem Pyramid Slide Down: https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python

def longest_slide_down(pyramid):
    
    hodl = []
    # bottom up approach, we start second to last row in the pyramid
    for i in range(len(pyramid)-2, -1, -1):
        # we iterate over every element one row lower to check for sums to store the biggest one
        for j in range(0,len(pyramid[i+1])-1):
            if pyramid[i][j] + pyramid[i+1][j] > pyramid[i][j] + pyramid[i+1][j+1]:
                hodl.append(pyramid[i][j] + pyramid[i+1][j])

            elif pyramid[i][j] + pyramid[i+1][j] <= pyramid[i][j] + pyramid[i+1][j+1]:
                hodl.append(pyramid[i][j] + pyramid[i+1][j+1])

        # replace the pyramid row with the row of possible sums and clean the hodling list
        pyramid[i] = hodl
        hodl = []
                
    
    return pyramid[i][i]
