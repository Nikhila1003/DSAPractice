from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1
    
sol = Solution()
print(sol.areOccurrencesEqual("abacbc"))

'''
Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true, because all characters appear twice. Given s = "aaabb", 
return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''