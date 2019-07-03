# define the fibonacci() function below...
def fibonacci(n):
	print(f"fibonacci({n})")
	if n == 0 or n == 1:
		print(f"Base Case for n == {n}")
		return n
	else:
		print(f"fibonacci({n - 2}) + fibonacci({n - 1})")
		return fibonacci(n - 2) + fibonacci(n - 1)



print(f"fibonacci({5}) = {fibonacci(5)}")
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"

# runtime: Exponential - O(2^N)

def fibonacci(n):
	if n < 0:
		ValueError("Input 0 or greater only!")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

			fibonacci(3)
# 2
fibonacci(7)
# 13
fibonacci(0)
# 0

def fibonacci(n):
	if n < 0:
		ValueError("Input 0 or greater only!")
	result = 0
	f1, f0 = 1, 0
	if n == 0 or n == 1:
		return n
	while n > 1:
		f2 = f0 + f1
		f1, f0 = f2, f1
		print(f"f2: {f2} pour n = {n}")
		n -= 1
	return f2


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)