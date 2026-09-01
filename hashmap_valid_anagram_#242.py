'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

# easiest solution and problem
# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"


def foo(s,t):

    from collections import Counter
    hmap1 = dict(Counter(s))
    hmap2 = dict(Counter(t))

    return hmap1==hmap2

print(foo(s,t))

'''
we can easily compare dictionaries like we do with lists
eg - 
dict1 = {'a':2,'b':3}
dict2 = {'b':3,'a':2}

print(dict1==dict2) => True
'''


# a better approach is without using hashing at all - checkout at last of this chat it uses integer indexing - https://claude.ai/chat/cd9110ff-1fbc-487f-b971-e25ec4ce52d7
# def foo(s, t):
#     if len(s) != len(t):
#         return False
#     counts = [0] * 26
#     for cs, ct in zip(s, t):
#         counts[ord(cs) - ord('a')] += 1
#         counts[ord(ct) - ord('a')] -= 1
#     return all(c == 0 for c in counts)