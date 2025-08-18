import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): 
            return False
        
        magazineDict = collections.Counter(magazine)
        
        for char in ransomNote:
            if magazineDict[char] <= 0:
                return False
            magazineDict[char] -= 1

        return True
    
sol = Solution()
print(sol.canConstruct("aa", "ab"))

'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote

Input: ransomNote = "a", magazine = "b"
Output: false

'''