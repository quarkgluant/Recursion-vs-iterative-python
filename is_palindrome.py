# Quadratic version - O(N^2)
# In each iteration of the loop that doesn’t return False, we make
#  a copy of the string with two fewer characters.
# Copying a list of N elements requires N amount of work in big O.
def is_palindrome_iter(my_string):
	while len(my_string) > 1:
		if my_string[0] != my_string[-1]:
			return False
		my_string = my_string[1:-1]
	return True

# Linear - O(N)
def is_palindrome(my_string):
    string_length = len(my_string)
    middle_index = string_length // 2
    for index in range(0, middle_index):
        opposite_character_index = string_length - index - 1
        if my_string[index] != my_string[opposite_character_index]:
            return False  
    return True

def palindrome(string):
    print(f"la chaine {string} est un palindrome? {is_palindrome(string)}")

palindrome("abba")
# True
palindrome("abcba")
# True
palindrome("")
# True
palindrome("abcd")
# False


def is_palindrome(my_string):
    if len(my_string) < 2:
        return True
    else:
        return False if my_string[0] != my_string[-1] else is_palindrome(my_string[1:-1])

palindrome("abba")
# True
palindrome("abcba")
# True
palindrome("")
# True
palindrome("abcd")
# False