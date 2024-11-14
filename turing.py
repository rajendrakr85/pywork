#given an array of integers, return the indices of the tow numbers that add up to a given target
#Constraints: are all the numbers positive or can there be negatives, are the duplicates numbers in array
flist=[1,3,7,6,4,8,5]
target=11

def findIndex(flist, target):
    for p1 in range(len(flist)):
        numberToFind = target - flist[p1]
        for p2 in range(p1+1,len(flist)):
            if numberToFind==p2:
                return p1, p2
             
    return -1, -1 


p1, p2 =findIndex(flist, target)         
#print('p1 = ',p1,'p2 = ',p2)


'''You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
Find two lines which together with the x-axis forms a container that would hold the greatest amount of a water. 
Return the area of water it would hold'''
heights = [7,1,2,3,9]
def holdingWater(wheights):
    maxArea = 0
    for p1 in range(len(wheights)):
        for p2 in range(p1+1,len(wheights)):
           height = min(wheights[p1],wheights[p2])
           width = p2 -p1
           area = height * width
           maxArea = max(maxArea, area)

    return maxArea

#print('Quantity of holding water :', holdingWater(heights))

def optimizeHoldingWater(wheights):
    p1=0
    p2= len(wheights)-1
    maxArea=0

    while(p1<p2):
        heights = min(wheights[p1], wheights[p2])
        weidth = p2 - p1;
        area = heights * weidth
        maxArea = max(maxArea, area)
        if(wheights[p1]<wheights[p2]):
            p1=p1+1
        else:
            p2=p2-1

    return maxArea


#print(optimizeHoldingWater(heights))


'''
     
'''
    
