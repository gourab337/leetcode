class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        #storing preprocessed nums
        nums = sorted(nums)
        hashmap = defaultdict(int)
        maxnumber = 0
        for i in nums:
            hashmap[i] +=  i
            maxnumber = max(i, maxnumber)
        @cache
        def maxProfit(i):
            if i == 0:
                return 0
            if i == 1:
                return hashmap[1]
            
            return max(maxProfit(i-1), maxProfit(i-2)+hashmap[i])
        
        return maxProfit(maxnumber)
