'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

def foo(s): # TC and SC - O(n) and O(n)
  return len(s.strip().split(" ")[-1])

################################################################
# TC and SC - O(n) and O(1)

s = "   fly me   to   the moon  "
def foo(s):
  i = len(s) - 1
  count = 0

  while i>=0 and s[i] == " ": ## Phase 1: skip trailing spaces
    i-=1
  while i>=0 and s[i] != " ": ## Phase 2: count the word
    i-=1
    count +=1
  return count


print(foo(s))

