#Python implementation of binary search
#Only works on a sorted array


def binary_search(arr,value):
	
	#At any given time, check everything between lo and hi
	lo = 0
	hi = len(arr)-1


	while lo <= hi:

		#Assigns middle index of the array each iteration
		midIndex = (lo+hi)//2
		midVal = arr[midIndex]

		if value == midVal:
			return midIndex

		#If value in question "left" of center, reassign window
		elif value < midVal:
			hi = midIndex - 1

		#Same with left side
		elif value > midVal:
			lo = midIndex + 1

	return -1


#Testing
mylist = [2,6,15,23,29,33,40,42,49,53,55]

#Should print a sequence from 1 : len(mylist)
for i in mylist:
	print(binary_search(mylist,i))

