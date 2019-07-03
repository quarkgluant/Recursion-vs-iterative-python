def find_min(my_list):
	min = None
	for element in my_list:
		if not min or (element < min):
			min = element
	return min

find_min([42, 17, 2, -1, 67])
# -1
find_mind([])
# None
find_min([13, 72, 19, 5, 86])
# 5

def find_min(my_list):
	middle_index = len(my_list) // 2
	if len(my_list) == 0:
		return None	
	elif len(my_list) == 1:
		return my_list[0]
	# elif len(my_list) == 2:
	# 	return my_list[0] if my_list[0] < my_list[1] else my_list[1]
	else:
		left = find_min(my_list[:middle_index]) 
		right = find_min(my_list[middle_index:]) 
		return left if left < right else right

