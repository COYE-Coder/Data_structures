#Python implementation of merge sort

import pprint
import numpy as np

#First define a split generator into n-sized lists using slices:
def split(arr,n):
	for i in range(0,len(arr),n):
		yield arr[i:i+n]
		#Will yield a 2D list of lists



#Then define a merging function that takes a list of lists and merges the two,
# Comparing each list elementwise
def merge(lists):
	iterate = range(0,len(lists),2)
	num_smalls = len(lists)

	#Define a list of empties
	mergedLists = [[] for num in range(num_smalls)]

	for listnum in iterate:
		i,j = 0, 0
		list1 = lists[listnum]
		list2 = lists[listnum+1]

		#While not reached the end of each component sublist
		while i < len(list1) and j < len(list2):
			if list1[i] < list2[j]:

				#Append to mergedLists the appropriate element
				mergedLists[listnum].append(list1[i])
				i += 1
			else:
				mergedLists[listnum].append(list2[j])
				j += 1


			#If reached the end of any given list, extends the sublist automatically
			if i >= len(list1):
				mergedLists[listnum].extend(list2[j:])
			
			elif j >= len(list2):
				mergedLists[listnum].extend(list1[i:])

	#Remove all empty lists
	mergedLists = [l for l in mergedLists if l != []]

	return mergedLists


#For readability, define another sorting function that sorts each split list 
	#-- Only needed for the sublist of size 2, but works for any size sublist
def sortSmall(lists):
	#Iterate over each n-sized lists
	for l in lists:

		#First ensure that the list isn't of len == 1
		if len(l) > 1:

			#Pairwise comparison of elements in each list
			for x,y in zip(l,l[1:]):


				#If leftward element is greater, switch the two
				if x > y:

					#Because we are using zip, we must find the indices
					i = l.index(x)
					j = l.index(y)
					l[i] = y
					l[j] = x
	return lists


def mergeSort(arr):
	n = len(arr)
	isNested = any(isinstance(el, list) for el in arr)


	#If input is already a list of lists, call recursively
	if isNested:
		if n > 1:

			mergedLists = merge(sortSmall(arr))
			mergeSorted = mergeSort(mergedLists)

			#If mergeSort returns anything, continue recursion
			if mergeSorted:
				return mergeSorted
			else:
				return mergedLists[0]


	#Using the split generator, divide lists into 2-sized lists to begin with		
	else:
		lists = list(split(arr,2))
		return mergeSort(lists)





	





arr = np.random.randint(0,50,size=8).tolist()

print("Original Array: " + str(arr))
print("Sorted? :")
print(str(mergeSort(arr)))


