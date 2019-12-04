def merge(arr1,arr2):
    p=len(arr1)
    q=len(arr2)-p
    i=0
    j=0
    count=0
    for count in range(len(arr2)):
        if(count<p):
            c=count+q
        else:
            c=count-p

        if(j==q or (i<p and arr1[i]<arr2[j])):
            arr2[c]=arr1[i]
            i=i+1
        elif(i==p or (j<q and arr1[i]>arr2[j])):
            arr2[c]=arr2[j]
            j=j+1

    print(arr2)

a=[1,2,3]
b=[-1,4,5,0,0,0]
merge(a,b)


def findindex(arr,start,end):
	#print(start,end)
	if(start>end):
		return
	mid=int((start+end)/2)
	if(end<mid+1):
		return -1	
	if(arr[mid]>arr[mid+1]):
		#print("xxx")
		return mid+1
	if(arr[start]<arr[mid]):
		return findindex(arr,mid,end)
	else:
		return findindex(arr,start,mid)
x=[i for i in range(10000)]
x.append(-1)
x.append(-2)
print(findindex(x,0,len(x)-1))
print("second test case")
x=[i for i in range(10000)]
print(findindex(x,0,len(x)-1))

