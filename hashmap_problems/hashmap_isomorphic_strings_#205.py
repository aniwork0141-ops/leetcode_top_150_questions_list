'''Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:
Input: s = "paper", t = "title"
Output: true
'''
# TC - O(n) and SC - O(k) where k is charset can say O(1) since its constant ceiling as keys would be definite only
def foo(s,t):
    forward = {}
    reverse = {}

    for x,y in zip(s,t):
        if x in forward:
            if forward[x] != y:
                return False
            # will skip else condition
        else:
            if y in reverse:
                # means someone already claimed this key in reverse (or value in forward)
                return False
            reverse[y] = x
            forward[x] = y
    return True


'''
s.find(ch) returns index of first occurrence.
'''


''' TC - O(n^2)
another interesting approach to solve this problem could be using list , in which i will just assign the first index the character was seen and compare both lists finally
'''
def goo(s,t):
    lst1 = [s.find(char) for char in s]
    lst2 = [t.find(char) for char in t]
    return lst1 == lst2

