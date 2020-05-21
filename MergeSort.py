#Python implementation of merge sort
#Not complete!!! Recursion needs changing
#Also need to change merge() to be smarter

import pprint
import numpy as np
import math

#First define a split generator into n-sized lists using slices:
def split(arr,n):
	for i in range(0,len(arr),n):
		yield arr[i:i+n]
		#Will yield a 2D list of lists



#Then define a merging function that takes a list of lists and merges the two,
# Comparing each list elementwise
def merge(lists):
	iterate = range(0,len(lists),2)

	mergedLists = [lists[i]+lists[i+1] for i in iterate if i+1 < len(lists)]

	return mergedLists


#For readability, define another sorting function that sorts each split list
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
	print("Is nested: " + str(isNested))


	#If input is already a list of lists, call recursively
	if isNested:
		sortedSmall = sortSmall(arr)
		mergedLists = merge(sortedSmall)

		mergeSorted = mergeSort(mergedLists)
		if len(mergeSorted) == 1:
			print("Merge Sort Completed")
			return list(mergeSorted)
		else:
			print("still sorting")


	#Using the split generator, divide lists into 2-sized lists to begin with		
	else:
		print("not nested")
		lists = list(split(arr,2))
		return mergeSort(lists)


	# #We know that the number of times an array of len N must be merged is:
	# # log2(N)-1
	# numMerges = math.ceil((math.log(n,2) - 1))
	# numIter = 0

	# while numIter <= numMerges:

	


	





arr = np.random.randint(0,50,size=8).tolist()

print("Original Array: " + str(arr))
print("Sorted? :")
mergeSort(arr)


