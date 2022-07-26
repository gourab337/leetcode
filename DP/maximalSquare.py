class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len (matrix[0])
        self.matrix = matrix
        
        dp = [[0 for i in range(n)] for j in range (m)]
        
        #dp[i][j] = largest square who's bottom right corner is at (i,j)
        #dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        
        @cache
        def ans(i,j):
            if ((i==0 or j==0) and self.matrix[i][j]=="1"):
                return 1
            elif (i<0 or j<0):
                return 0
            elif (self.matrix[i][j] == "0"):
                return 0
            else:
                return min(ans(i-1,j-1), ans(i-1,j), ans(i,j-1)) + 1
                
        max_ans = 0
        # O(mxn) 
        for i in range(m):
            for j in range(n):
                dp[i][j] = ans(i,j)
                max_ans = max(max_ans, dp[i][j])
    
        return max_ans*max_ans
