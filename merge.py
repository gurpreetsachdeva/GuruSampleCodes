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



def search_rotated_array(a,key):
	index=findindex(a,0,len(a)-1)
	if(index==-1):
		return binarysearch(a,0,len(a),key)
	elif(key>a[0] and key <a[index-1]):
		return binarysearch(a,0,index-1,key)
	else:
		return binarysearch(a,index,len(a)-1,key)
def binarysearch(a,start,end,key):
	#print(start,end)
	if(start>end):
		return False
	mid=int((start+end)/2)
	if(a[mid]==key):
		return (True,mid)
	if(a[mid]<key):
		return binarysearch(a,mid+1,end,key)
	else:
		return binarysearch(a,start,mid,key)
print("**********************************************")

a=[1,2,3]
b=[-1,4,5,0,0,0]
#print(merge(a,b))
print("**********************************************")


x=[i for i in range(10000)]
x.append(-1)
x.append(-2)
print(findindex(x,0,len(x)-1))
print("second test case")
x=[i for i in range(10000)]
print(findindex(x,0,len(x)-1))

print("***************************************")
print(binarysearch([1,2,3,4,5],0,4,10))

print("First Test Case")
print(search_rotated_array([7,8,9,1,2,3],8))
print("Second test case")
print(search_rotated_array([7,8,9,1,2,3],10))
