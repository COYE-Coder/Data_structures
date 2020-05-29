import numpy as np


#Python implementation of quicksort


def quicksort(arr,lo=0,hi=False):
	if not hi:
		hi = len(arr)

	arr = arr[lo:hi]
	arr_length = len(arr)

	print("Array at top: {}".format(arr))
	if arr_length < 3:
		return arr


	if arr_length > 3:
		#Find median of last n elements in arr
		last_n = np.array(arr[-3:])

		#Set median as pivot
		pivot = int(np.percentile(last_n,50))
		print("Pivot = {}".format(pivot))

		#Guarantee to find the "right-most" pivot index
		pivot_index = arr.index(pivot,arr_length-3,arr_length)
		

	else:
		pivot = arr[-1]
		print("Pivot = {}".format(pivot))
		pivot_index = len(arr)-1


	#Compare pivot to all elements to the left
	#Stops when pivot has reached the same index that it will be evaluated against
	i = 0
	while i < pivot_index:
		checked_element = arr[i]
		#If first element belongs on the right
		while checked_element > pivot:
			#First store all relevant values
			left_of_p = arr[pivot_index-1]
			


			#Perform switch
			arr[pivot_index] = checked_element
			arr[i] = left_of_p
			arr[pivot_index-1] = pivot

			#Change checked element
			checked_element = arr[i]

			#Increment pivot index
			pivot_index -= 1
		print("Array during while: {}".format(arr))

		#Increment index- changes checked_element if pivot < c_e
		i += 1
	print("Pivot Index: {} ".format(pivot_index))



	#If split concurs a small enough array, all pivots should be sorted

	#Need to store original arr somewhere -- always returns None
	print("Array: {}".format(arr))
	left_half_sorted = quicksort(arr,0,pivot_index)
	right_half_sorted = quicksort(arr,pivot_index,len(arr)-1)
	print("Left Half: {} \nRight Half: {}".format(left_half_sorted,right_half_sorted))
	return left_half_sorted+right_half_sorted
	







nested = np.random.randint(0,50,size=8).tolist()
arr = [0, 4, 34, 17, 11, 49, 35, 38]
print(quicksort(nested))
# print(nested)
# print(quicksort(nested))



