# def foo(nums):
#   new_list = []
#   for i in nums:
#     prod = 1
#     for j in nums:
#       if i!=j:
#         prod*=j
#     new_list.append(prod)
#   return new_list

# print(foo(nums))
"""missed the case where the elements could all be same , so cant compare i with j in that case as it would use the default value of prod since will not go inside if condition"""

######################################################################################

"""one thing i can try , instead of using the actual value for comparing i and j , i could use their index so that i can still skip the same index"""

# def foo(nums):
#   new_list = []
#   for i in range(len(nums)):
#     prod = 1
#     for j in range(len(nums)):
#       if i!=j:
#         prod*=nums[j]
#     new_list.append(prod)
#   return new_list

# print(foo(nums))

"""although this above solution worked , but has the TLE issue , due to O(n^2) Time complexity , need to optimize it now to O(n)"""

######################################################################################

def foo(nums):
  res = [1]*len(nums)
  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
  postfix = 1
  for i in range(len(nums)-1,-1,-1):
    res[i] *= postfix
    postfix *= nums[i]
  return res

print(foo(nums))

"""The Core Strategy:
Since division is not allowed, the solution calculates the product of all elements to the left and all elements to the right for every position in the array.

Prefix Pass (Left to Right):

You create an output array initialized with 1s.
Iterate through the array from the beginning to the end, storing the running product of all elements encountered so far in the output array.
For example, at index i, the result array will contain the product of all numbers from index 0 to i-1.
Postfix Pass (Right to Left):

Iterate backward from the end of the array to the beginning.
Maintain a running product of elements to the right of the current index (initialized at 1).
Multiply the current value in the output array (which holds the prefix product) by the running postfix product.
Update the running postfix product by multiplying it with the value at the current index in the original input array.
By the end of the second pass, every index in the result array contains the product of all numbers in the input array except for the number at that specific index.

=> followed this solution by neetcode : https://www.youtube.com/watch?v=bNvIQI2wAjk"""
