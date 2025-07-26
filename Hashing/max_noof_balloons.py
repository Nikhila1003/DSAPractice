from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon_dict = {'a': 0, 'b': 0, 'l': 0, 'n': 0, 'o': 0}
        
        for char in text:
            if char in ballon_dict:
                ballon_dict[char] += 1
        
        ballon_dict['l'] //= 2
        ballon_dict['o'] //= 2
        
        counts = ballon_dict.values()
        min_count = min(counts)
        
        return min_count

sol = Solution()
print(sol.maxNumberOfBalloons("nlaebolko"))

'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''