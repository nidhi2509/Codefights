def shapeArea(n):
    
    j = 0
    for i in range(1,(n-1)*2,2):
        
        j = j + i
    
    return ((2*j)+(2*n)-1)
