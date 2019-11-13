# Linear Search Example : 
# Return -1 if the item is not found, otherwise return the index for the item
# Time Complexity O(n)
# Space Complexity O(n)
def linear_search(items,x):
	for i in range(0,len(items)):
		if(items[i]==x):
			return i
	return -1
