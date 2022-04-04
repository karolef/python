# codewars problem Pyramid Slide Down: https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python

def longest_slide_down(pyramid):
    print(pyramid)
    hodl = []
    for i in range(len(pyramid)-2, -1, -1):

        for j in range(0,len(pyramid[i+1])-1):
            if pyramid[i][j] + pyramid[i+1][j] > pyramid[i][j] + pyramid[i+1][j+1]:
                hodl.append(pyramid[i][j] + pyramid[i+1][j])

            elif pyramid[i][j] + pyramid[i+1][j] <= pyramid[i][j] + pyramid[i+1][j+1]:
                hodl.append(pyramid[i][j] + pyramid[i+1][j+1])

            
        pyramid[i] = hodl
        hodl = []
                
    
    return pyramid[i][i]
