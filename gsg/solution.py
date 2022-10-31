"""
Intro: John has bought a new house and found a diary of the previous house owner, describing a single trip. 
       Also there were tickets inside with source and destination points, but without dates.Help John find the 
       original route of the trip. 
Task: Write a function that accepts array of tickets, where ticket has format [source: string, destination: string] 
      and returns comma separated countries in order of visiting. 
 
Example: ---> tickets: [["JPN", "PHL"], ["BRA", "UAE"], ["USA", "BRA"], ["UAE", "JPN"]]
result: "USA, BRA, UAE, JPN, PHL"
"""
import collections

class Solution: 

    def findOriginalRouteOfTrip(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['USA']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]

solution = Solution()
tickets = [["JPN", "PHL"], ["BRA", "UAE"], ["USA", "BRA"], ["UAE", "JPN"]]    
print(solution.findOriginalRouteOfTrip(tickets))