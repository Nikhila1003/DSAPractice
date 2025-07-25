from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners_result = set()
        losers_result = set()
        total_losers = set()
        
        for match in matches:
            match_winner = match[0]
            match_loser = match[1]
            
            if match_winner not in total_losers and match_winner not in winners_result:
                winners_result.add(match_winner)
            
            if match_loser not in total_losers and match_loser not in losers_result:
                losers_result.add(match_loser)
            elif match_loser in total_losers and match_loser in losers_result:
                losers_result.remove(match_loser)
            
            if match_loser in winners_result:
                winners_result.remove(match_loser)
            
            total_losers.add(match_loser)
        
        winners_result = list(winners_result)
        losers_result = list(losers_result)
        winners_result.sort()
        losers_result.sort()
        
        return [winners_result, losers_result]
    
sol = Solution()
print(sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

'''