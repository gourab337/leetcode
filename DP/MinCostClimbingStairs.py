class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(i):
            if i<= 1:
                return 0;
            if i not in hashmap:
                hashmap[i] = min(dp(i-2)+cost[i-2], dp(i-1)+cost[i-1])
            return hashmap[i]
        hashmap = {}
        return dp(len(cost))
