class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z'}
        sentence_set = set(sentence)
        
        for char in alphabets:
            if char not in sentence_set:
                return False

        return True

sol = Solution()
print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

'''
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Input: sentence = "leetcode"
Output: false
'''