height = [1,7,2,5,4,7,3,6]

# height = [1,2]
'''### brute force approach ###
def foo(height):
  if len(height)==0:
    return 0
  maxar = 0
  for i in range(len(height)):
    for j in range(i+1,len(height)):
      ht = min(height[i],height[j])  
      wt = j - i
      ar = ht * wt
      maxar = max(maxar,ar)
  return maxar

print(foo(height))
'''

### optimization ###

i=0
n = len(height)
j=n-1
maxar=0
while j>i:
  maxar = max((j-i)*(min(height[j],height[i])),maxar)
  if height[i] < height[j]:
    i+=1
  else:
    j-=1
print(maxar)
    
    
