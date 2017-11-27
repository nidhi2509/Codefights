def allLongestStrings(inputArray):
    li = []
    maxi = ""
    maxlen = max(len(i) for i in inputArray)
    li = [i for i in inputArray if len(i) == maxlen]
            
    
            
    return li
