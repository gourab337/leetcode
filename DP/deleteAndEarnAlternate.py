class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        #storing preprocessed nums
        nums = sorted(nums)
        profits = defaultdict(int)
        maxnumber = 0
        for i in nums:
            profits[i] +=  i
            maxnumber = max(i, maxnumber)
        
        def maxProfit(i):
            if i == 0:
                return 0
            if i == 1:
                return profits[1]
            
            if i not in hashmap:
                hashmap[i] = max(maxProfit(i-1), maxProfit(i-2)+profits[i])
            return hashmap[i]
        
        hashmap = {}
        return maxProfit(maxnumber)
