def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    
    print(call_stack)
    print(f"add return_value[\"n_value\"] ({execution_context}) to result: {result}")
    result += execution_context['n_value']
    n -= 1
  print("BASE CASE REACHED")
  while call_stack:
    return_value = call_stack.pop()

    print(f"call_stack: {call_stack}")
  return result, call_stack

def sum_to_one_rec(n):
  return 1 if n == 0 else n + sum_to_one_rec(n - 1)

sum_to_one(4)