def selectsort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(arr[min]>arr[j]):
                min=j
        if(i!=min):
            temp=arr[i]
            arr[i]=arr[min]
            arr[min]=temp

    print(arr)
def bubblesort(arr):
    n=len(arr)
    flag=1
    for i in range(n-1):
        if(flag==1):
            flag=0
        else:
            break;
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                flag=1

    print(arr)
