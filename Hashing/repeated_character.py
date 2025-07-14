class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "

sol = Solution()
print(sol.repeatedCharacter('abcdeda'))

'''
First Letter to Appear Twice

Given a string s, return the first character to appear twice. 
It is guaranteed that the input will have a duplicate character.
'''