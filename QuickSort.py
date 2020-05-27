import numpy as np


#Python implementation of quicksort


def quicksort(arr):
	arr_length = len(arr)


	#Find median of last 3 elements in arr
	last_three = np.array(arr[-3:])

	#Set median as pivot
	pivot = int(np.percentile(last_three,50))

	#Guarantee to find the "right-most" pivot index
	pivot_index = arr.index(pivot,arr_length-3,arr_length)
	
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
			print(pivot_index)
			print(arr)

		#Increment index
		i += 1
	print(arr)
		# After we guarantee that the pivot is > first element,
		# we set the checked_element to be the next element






# nested = np.random.randint(0,50,size=8).tolist()
arr = [35, 39, 49, 17, 4, 0, 11, 9]
print(arr)
quicksort(arr)

# arr_length = len(arr)
# last_three = np.array(arr[-3:])
# pivot = int(np.percentile(last_three,50))
# pivot_index = arr.index(pivot,arr_length-3,arr_length)

# i = 0
# checked_element = arr[i]

# print(checked_element > pivot)

# left_of_p = arr[pivot_index-1]
# print(left_of_p)

# arr[pivot_index] = checked_element
# print(arr)			
# arr[i] = left_of_p
# checked_element = arr[i]
# print(arr)
# arr[pivot_index-1] = pivot
# print(arr)

# pivot_index -= 1

# print("//========================================================")

# left_of_p = arr[pivot_index-1]
# print(left_of_p)

# arr[pivot_index] = checked_element
# print(arr)			
# arr[i] = left_of_p
# print(arr)
# arr[pivot_index-1] = pivot
# checked_element = arr[i]

# print(arr)

# pivot_index -= 1


# print(checked_element > pivot)

# #Increment checked element
# i+= 1
# checked_element = arr[i]

# print("//========================================================")
# print(checked_element)
# left_of_p = arr[pivot_index-1]
# print(left_of_p)
# arr[pivot_index] = checked_element
# print(arr)
# arr[i] = left_of_p
# arr[pivot_index-1] = pivot
# print(arr)
# checked_element = arr[i]
# pivot_index-=1

# print(checked_element > pivot)

# #Increment checked element
# i+= 1
# checked_element = arr[i]
# print("//========================================================")
# print(checked_element)


# print(checked_element > pivot)

# left_of_p = arr[pivot_index-1]
# print(left_of_p)
# arr[pivot_index] = checked_element
# print(arr)
# arr[i] = left_of_p
# print(arr)
# arr[pivot_index-1] = pivot
# print(arr)
# checked_element = arr[i]

# pivot_index -= 1

# print(checked_element > pivot)

# print("//========================================================")
# print("pivot_index: " + str(pivot_index))
# left_of_p = arr[pivot_index-1]
# print(left_of_p)

# arr[pivot_index] = checked_element
# print(arr)
# arr[i] = left_of_p
# print(arr)
# arr[pivot_index-1] = pivot
# print(arr)
# checked_element = arr[i]

# pivot_index -= 1
# print(pivot_index)
# print(i)

# print(checked_element > pivot)









