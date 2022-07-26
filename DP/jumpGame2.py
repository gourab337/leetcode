class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            if i == len(nums)-1:
                return 0
            else:
                ans = len(nums)+100
                
                for jumpStep in range(1, nums[i]+1):
                    if i+jumpStep >= len(nums):
                        break
                    ans = min(ans, 1+ dp(i+jumpStep))
                    
                return ans
                
