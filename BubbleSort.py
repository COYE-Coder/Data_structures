#Python implementation of a naive bubble sort
#Has time complexity O(n^2)

import numpy as np

def bubbleSort(arr):

	#Stores the number of less than pairs
	numLess = 0
	i = -1
	j = 0

	while numLess < len(arr)-1:
		
		#Starts iterating at i = 0, j =1
		i += 1
		j = i+1

		#If j is at the end of the list, iterate from beginning
		#Start iterating over again
		if j > len(arr)-1:
			numLess = 0
			i = 0
			j = 1


		e1 = arr[i]
		e2 = arr[j]

		#If right-wards element is less, switch the two
		if e1 > e2:
			arr[i] = e2
			arr[j] = e1

		else:
			numLess += 1
	
	return arr

			

arr = np.random.randint(0,50,size=10).tolist()
print(arr)

sortedArr = bubbleSort(arr)


print ("Sorted Array: " + str(sortedArr))

