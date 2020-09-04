class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0
        
        for num in nums:
            once = ~twice &(once ^ num)
            twice = ~once & (twice^num)
        return once
        
        
 **********************************
 
 class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
******************************************

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count = collections.Counter(nums)
        
        for num in count:
            if count[num] == 1:
                return num
