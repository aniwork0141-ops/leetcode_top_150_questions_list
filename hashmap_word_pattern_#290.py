'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.'''


def foo(pattern,s):
    hmapfwd = {}
    hmapbwd = {}
    s_list=s.split(' ')

    if len(s_list) != len(pattern):
        return False

    for x,y in zip(pattern,s_list):
        if x in hmapfwd:
            if hmapfwd[x] != y:
                return False
        else:
            #means key not present in map now
            if y in hmapbwd:
                return False
                #means this y exists in bwd map as key
            hmapfwd[x] = y
            hmapbwd[y] = x

    return True


'''EXPLANATION FOR THE 2nd IF CONDITION with y in hmapbwd

hmapbwd[y] is a pattern letter. You're inside the branch where x is new — not in hmapfwd. And you always write both maps together, so:

x in hmapfwd ⟺ x is a value in hmapbwd.

So since x is new, x appears as a value in hmapbwd nowhere. Nothing to check.

Now the reverse question — the case you do handle:

y in hmapbwd and x new. Then hmapbwd[y] is some other letter, call it z, with z != x. That means z → y already, and now you want x → y too. Two letters, one word. Bijection dead. Return False.

Hashing. String hash reads every char. Word of length L → O(L). Not O(1). Also comparison hmapfwd[x] != y compares strings — O(L) too.


### TC AND SC : 

Time: O(m), m = len(s). Split + hashing/comparing words.
Space: O(m) as written (s_list dominates). Maps alone are O(1) since bounded by 26.

'''