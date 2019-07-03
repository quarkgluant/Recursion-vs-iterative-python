def power_set_iter(set):
  power_set_size = 2**len(set)
  result = []
#   set = ['a', 'b', 'c']
#   binary_number = "101"
#   produces the subset ['a', 'c']
#   'b' is left out because its binary digit is 0
# The iterative approach uses this insight 
# for a very clever solution by including an element
#  in the subset if its “binary digit” is 1
  for bit in range(0, power_set_size):
    sub_set = []
    for binary_digit in range(0, len(set)):
      if((bit & (1 << binary_digit)) > 0):
        sub_set.append(set[binary_digit])
    result.append(sub_set)
  return result

def power_set_rec(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set_rec(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first

  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set_rec(universities)

for set in power_set_of_universities:
  print(set)