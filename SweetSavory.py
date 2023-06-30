"""
Sweet And Savory✩
You're hosting an event at a food festival and want to showcase the best possible pairing of two dishes from the festival that complement each other's flavor profile.
Each dish has a flavor profile represented by an integer. A negative integer means a dish is sweet, while a positive integer means a dish is savory. The absolute value of that integer represents the intensity of that flavor. For example, a flavor profile of -3 is slightly sweet, one of -10 is extremely sweet, one of 2 is mildly savory, and one of 8 is significantly savory.
You're given an array of these dishes and a target combined flavor profile. Write a function that returns
"""

def sweetAndSavory(dishes, target):
    # Write your code here.
    best = [0,0]
    print("print the list withoput sorting = " , dishes)
    sweetDishes = sorted([dish for dish in dishes if dish < 0] , key = abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0 ])
    if len(sweetDishes) == 0 or len(savoryDishes) == 0:
        return best

    print("print sweet dish list = ", sweetDishes)
    print("print savory dish list = ", savoryDishes)
    indexSweet , indexSavory = 0 , 0
    bestDif = savoryDishes[-1] - sweetDishes[-1] + target + target
    print("print the best dif = ", bestDif)
    print("print length of sweet list = " , len(sweetDishes), " and length of savory list = " , len(savoryDishes) )
    while indexSweet < len(sweetDishes ) and indexSavory < len(savoryDishes) :
        
        sum = sweetDishes[indexSweet] + savoryDishes[indexSavory]

        if sum > target:
            indexSweet += 1
        else:
            curDif = abs(target - sum)
            if curDif < bestDif:
                bestDif = curDif
                best = [sweetDishes[indexSweet], savoryDishes[indexSavory] ]
            indexSavory += 1
    print ("the final answer is = ", best)
    return best
    
