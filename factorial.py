def factorial(n):
	if n < 0:    
		ValueError("Inputs 0 or greater only") 
	result = n
    for i in range(1, n):
        result *= i
    return result if n > 0 else 1

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)

# runtime: Linear - O(N)
def factorial(n):  
	if n < 0:    
		ValueError("Inputs 0 or greater only") 
    if n <= 1:    
        return 1  
    return n * factorial(n - 1)

factorial(3)
# 6
factorial(4)
# 24
factorial(0)
# 1
factorial(-1)
# ValueError "Input must be 0 or greater"