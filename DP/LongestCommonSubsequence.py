class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def LCS(text1,text2, m, n):
            if (m==0 or n==0):
                return 0
            if(text1[m-1]==text2[n-1]):
                return 1 + LCS(text1,text2,m-1,n-1)
            else: 
                return max(LCS(text1,text2,m-1,n), LCS(text1,text2,m,n-1))
            
