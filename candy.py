# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
'''
1. Distribute 1 candy to each child in the starting
2. Then just comapre each child with its left neighbour and alot based on that
3. Then start from the end and check, if the current value at that index > than 1+neighbour, if it is let it be

'''
class Solution:
    def candy(self, ratings):
        if len(ratings) < 1:
            return 0 
        
        nums = [1 for _ in range(len(ratings))]

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1 
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                nums[i] = max(nums[i], nums[i]+nums[i+1])
        print(nums)
        candies = 0 
        for candy in nums:
            candies += candy 
        
        return candies