'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        for item in strs:
            key = ''.join(sorted(item))
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(item)
        return list(hmap.values())



'''
or could use defaultdict from collections library

Normal dict: missing key → KeyError.
defaultdict(list): missing key → calls list() → inserts [] → then proceeds.

Code:
from collections import defaultdict
hmap = defaultdict(list)
for item in strs:
    key = ''.join(sorted(item))
    hmap[key].append(item)
return list(hmap.values())
'''
