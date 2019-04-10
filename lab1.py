
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
   	return None
   if int_list == None:
   	raise ValueError
   maxi = int_list[0]
   for i in range(len(int_list)):
   	if int_list[i] >= maxi:
   		maxi = int_list[i]
   return maxi



def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
   	raise ValueError
   if int_list == []:
   	return []
   reversed_list = []
   reversed_list.append(int_list[-1])
   return reversed_list + (reverse_rec(int_list[:-1]))


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
   	raise ValueError
   if low > high:
   	return None
   mid = (high + low) // 2
   if int_list[mid] == target:
   	return mid
   if target < int_list[mid]:
   	return bin_search(target, low, mid - 1, int_list)
   else: return bin_search(target, mid + 1, high, int_list)

print(max_list_iter([1,2,5,67]))