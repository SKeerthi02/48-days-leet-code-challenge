class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        target1 = collections.defaultdict(int)
        target2 = collections.defaultdict(int)
        
        for num in nums1:
            target1[num*num] += 1
        for num in nums2:
            target2[num*num] += 1
            
        count = 0
        for i in range(len(nums1)):
            for k in range(i+1, len(nums1)):
                c = nums1[i] * nums1[k]
                if c in target2:
                    count += target2[c]
        for i in range(len(nums2)):
            for k in range(i+1, len(nums2)):
                c = nums2[i] * nums2[k]
                if c in target1:
                    count += target1[c]
        return count
        
