class Solution:
    
    def isRepeated(self,mid, n, S):
        seen = set()
        for i in range(0, n-mid+1):
            if S[i:i+mid] in seen:
                return i
            seen.add(S[i:i+mid])
        return -1
    def longestRepeatingSubstring(self, S: str) -> int:
        
        n = len(S)
        
        left = 1
        right = n 
        while left <=right:
            
            mid = left + (right - left) // 2
            
            if self.isRepeated(mid, n, S) != -1:
                left = mid + 1
            else:
                right = mid - 1
            
        
        return left - 1
