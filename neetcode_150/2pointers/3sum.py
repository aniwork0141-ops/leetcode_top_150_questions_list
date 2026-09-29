
##############################brute force approach O(n cube)
# nums = [-1,0,1,2,-1,-4]
# out=[]
# for i in range(len(nums)):
#   for j in range(i+1,len(nums)):
#     for k in range(j+1,len(nums)):
#       if (nums[i] + nums[j] + nums[k] == 0) and (sorted([nums[i],nums[j],nums[k]]) not in out):
#         out.append([nums[i],nums[j],nums[k]])

# print(out)
#############################################################
"""
sort the input array
"""

nums = [-1,0,1,2,-1,-4]

# nums.sort()
# print(nums)
# out=[]
# for i in range(len(nums)):
#   j=i+1
#   k=len(nums)-1
#   while j<k and k>i:
#     print("j=",nums[j],"k=",nums[k])
#     target = -nums[i]
#     if (nums[j] + nums[k] == target) and ([nums[i],nums[j],nums[k]] not in out):
#       out.append([nums[i],nums[j],nums[k]])
#       j+=1
#       k-=1
      
#     elif nums[j] + nums[k] < target:
#       j+=1
#     else:
#       k-=1

# print(out)
  
##########################################Optimized approach

nums = [-1,0,1,2,-1,-4]
# def foo(nums):
#   nums.sort()
#   n = len(nums)
#   out=[]
#   for i in range(n-2):
#     if nums[i] > 0: #means smallest item is >0 so early  exit
#       break #check why used break here
#     if i>0 and nums[i]==nums[i-1]:
#       continue #check why used continue here
#     j=i+1
#     k=n-1

#     while j<k:
#       total = nums[i] + nums[j] + nums[k]

#       if total == 0:
#         out.append([nums[i] ,nums[j] ,nums[k]])

#         while j<k and nums[j]==nums[j+1]:
#           j+=1
#         while j<k and nums[k]==nums[k-1]:
#           k-=1
#         j+=1
#         k-=1
#       elif total<0:
#         j+=1
#       else:
#         k-=1
#     return out


########################################

def foo(nums=[-1,0,1,2,-1,-4]):
  nums.sort()
  out = []
  n = len(nums)

  for i in range(n - 2):
      # Optimization 1: Early exit — if the smallest element is > 0, sum cannot be 0
      if nums[i] > 0:
          break

      # Optimization 2: Skip duplicates for 'i' without checking the output list
      if i > 0 and nums[i] == nums[i - 1]:
          continue

      j = i + 1
      k = n - 1

      while j < k:
          total = nums[i] + nums[j] + nums[k]

          if total == 0:
              out.append([nums[i], nums[j], nums[k]])

              # Optimization 3: Skip duplicate elements for 'j' and 'k'
              while j < k and nums[j] == nums[j + 1]:
                  j += 1
              while j < k and nums[k] == nums[k - 1]:
                  k -= 1

              j += 1
              k -= 1

          elif total < 0:
              j += 1
          else:
              k -= 1

  return out

print(foo(nums))
    
