class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1 = nums1 + nums2
        
        nums1.sort()
        print(nums1)
        if len(nums1) % 2 == 1:
            return nums1[int(len(nums1)//2)]
        else:
            n = int(len(nums1)//2)
            return (nums1[n-1] + nums1[n])/2
            
            
            
    ********************************************************************
    
    class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m, n = len(nums1), len(nums2)
        
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        
        imin, imax, mid = 0, m, int((m+n+1)/2)
        
        while imin <= imax:
            
            i = int((imax+imin)/2)
            j = mid - i
            
            if i < m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imin = i-1
            else:
                if i == 0: 
                    maxOfLeft = nums2[j-1]
                elif j == 0:
                    maxOfLeft = nums1[i-1]
                if (m+n) % 2 == 1:
                    return maxOfLeft
                
                if i ==m: minofright = nums2[j]
                elif j == n: minofright = nums1[i]
                else: minofright = min(nums1[i], nums2[j])
                
                return (maxOfLeft + minofright)/ 2.0
