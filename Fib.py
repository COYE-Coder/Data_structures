#Will return the fibonacci number at a given position
#ex: compute_fib(6) => 8
# fib_list => [0,1,1,2,3,5,*8*]
#Computes both recursively and with a list
#Compares the two with scipy

from timeit import default_timer as timer
import statistics
from scipy import stats



def compute_fib(pos):

	if pos < 0:
		return -1

	elif pos == 0 or pos == 1:
		return pos

	fibArr = [0]
	num1 = 0
	num2 = 1

	while len(fibArr)-1 != pos:
		fibArr.append(num1+num2)
		num1 = fibArr[-1]
		num2 = fibArr[-2]

	return num1


#Recursive function:

def compute_fib_recursive(pos):
	if pos == 0 or pos == 1:
		return pos

	return compute_fib_recursive(pos-1) + compute_fib_recursive(pos-2)



#Test of a significant difference:
def test_two(func1,func2,n):
	times1 = []
	times2 = []

	#Test first function
	i = 0
	while i < n:
		start = timer()
		x = func1
		i+= 1
		end = timer()

		times1.append(end-start)

	#Test second function
	i = 0
	while i < n:
		start = timer()
		x = func2
		i+= 1
		end = timer()

		times2.append(end-start)
	
	return times1, times2


times1,times2 = test_two(compute_fib(10),compute_fib_recursive(10),100)
print("Mean Time for compute_fib: " + str(statistics.mean(times1)))
print("Mean Time for compute_fib_recursive: " + str(statistics.mean(times2)))


#There is a significant difference in performance of an order of magnitude
print(stats.ttest_ind(times1,times2))


