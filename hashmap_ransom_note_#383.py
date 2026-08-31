'''
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

# Brute Force approach - Time Complexity O(n*m) 

def canConstructBruteForce(ransomNote: str, magazine: str) -> bool:
    magazine_list = list(magazine)
    for char in ransomNote:
        if char in magazine_list:
            magazine_list.remove(char)
        else:
            return False
    return True

# Optimized Approach using Hashmap O(1) lookup , time O(m + n), space O(1).

def canConstructOptimized(ransomNote:str,magazine:str):
    hmap = {}
    for char in magazine:
        if char not in hmap:
            hmap[char]=1
        else:
            hmap[char]+=1

    for char in ransomNote:
        # if char in hmap and hmap[char]>0: #use below .get logic instead of this , its better
        if hmap.get(char,0):
            hmap[char]-=1
        else:
            return False
    return True


ransomNote = "ab"
magazine = "ab"

print(canConstructBruteForce(ransomNote,magazine))
print(canConstructOptimized(ransomNote,magazine))

'''
instead of traversing the hmap and populating it , i could use the python's Collections.counter

example of that - 

from collections import Counter
# Create a list of items
a = [1, 1, 1, 2, 3, 3, 4]

# Use Counter to count occurrences
cnt = Counter(a)
print(cnt) => Counter({1: 3, 3: 2, 2: 1, 4: 1})
'''