class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        # dp[d][i] = from ith job, find the min sum of max values in each of #d sub arrays
        # ans = dp[d][0]
        # recurrence relation = min(max(jD[j: n-d+1] + dp(d-1, j+1)))
        
        numOfJobs = len(jobDifficulty)
        if numOfJobs < d:
            return -1
        @cache
        def dp(d,i):
            if d==1:
                return max(jobDifficulty[i:])
            
            maxSoFar = 0
            ans = float('inf')
            for j in range (i, numOfJobs-d+1):
                maxSoFar = max(maxSoFar, jobDifficulty[j])
                ans = min(ans , maxSoFar + dp(d-1, j+1))
            return ans
        
        return dp(d,0)
