inputs  = [[12,0,21,14,0,23],[0,45,8,0,94,9],[35,0,13,10,0,38],[0,26,8,0,9,25]]
inputs2 = [[0,5,9,0,9,7],[0,15,11,0,20,16],[26,0,10,39,0,23],[37,0,5,30,0,11],[41,0,0,28,0,13]]

## original questions, two circles are both on x-axis or on y-axis
def twoCircle (inputs):
    resultList =[]
    for tempInput in inputs:
        x1, y1, r1, x2, y2, r2 = tempInput
        if x1 == x2 == 0:
            x1,y1,x2,y2=y1,x1,y2,x2
        if r1 < r2:
            r1,r2=r2,r1
        centerDist= abs(x1-x2)
        if x1==x2:
            resultList.append('concentric')
        elif centerDist == r1+r2 or centerDist == r1-r2:
            resultList.append('touching')
        elif centerDist > r1 + r2:
            resultList.append('Disjoint-outside')
        elif centerDist < r1 - r2:
            resultList.append('Disjoint-inside')
        else:
            resultList.append('Intersecting')
    return resultList

res=twoCircle(inputs)
print(res)
res=twoCircle(inputs2)
print(res)