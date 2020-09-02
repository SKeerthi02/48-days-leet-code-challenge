class Solution:
    
    def expand(self, left, right, s):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        left , right = 0, 0
        
        
        for i in range(len(s)):
            
            len1 = self.expand(i, i, s)
            len2 = self.expand(i, i+1, s)
            
            length = max(len1, len2)
            
            if length > right - left:
                left = i- int((length - 1)/2)
                right = int(i+ length/2)
        return s[left: right+1]
