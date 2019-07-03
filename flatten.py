# define flatten() below...
def flatten(my_list):
  result = flat_list = []
  for lst in my_list:
    if isinstance(lst, list):
      print("List found!")
      flat_list = flatten(lst)
      result += flat_list
    else:
      result.append(lst)
  return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))