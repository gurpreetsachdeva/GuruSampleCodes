def pairs(k, arr):
    t={}
    arr.sort()
    count=0
    for i in arr:
        t[i]=i
    for i in arr:
        if(t.get(i+k,None)!=None):
            count=count+1 
        #if(t.get(i-k,None)!=None):
            #count=count+1 


    return count
