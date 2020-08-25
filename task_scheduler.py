# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def leastInterval(self, tasks, n):
        maxFreq, maxCount = 0 , 0 
        map_ = {}

        for c in tasks:
            if c not in map_:
                map_[c] = 0
            map_[c] += 1 
            maxFreq = max(maxFreq, map_[c])
        
        
        for k,v in map_.items():
            if v == maxFreq:
                maxCount += 1 
        
        partitions = maxFreq - 1 
        empty = (n - (maxCount - 1)) * partitions
        pending = len(tasks) - maxFreq * maxCount
        idle = max(0, empty - pending)
        return idle + len(tasks)
