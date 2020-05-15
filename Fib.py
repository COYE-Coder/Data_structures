#Will return the fibonacci number at a given position
#ex: compute_fib(6) => 8
# fib_list => [0,1,1,2,3,5,*8*]

def compute_fib(pos):

	if pos < 0:
		return -1

	elif pos == 0:
		return 0

	elif pos == 1:
		return 1

	fibArr = [0]
	num1 = 0
	num2 = 1

	while len(fibArr)-1 != pos:
		fibArr.append(num1+num2)
		num1 = fibArr[-1]
		num2 = fibArr[-2]

	return num1

test = []
for i in range(50):
	test.append(compute_fib(i))

print(test)