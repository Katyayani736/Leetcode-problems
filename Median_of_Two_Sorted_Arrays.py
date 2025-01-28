class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        i,j=0,0
        e=0
        prev=0
        for c in range(0,(n+m)//2+1):
            prev=e
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    e=nums2[j]
                    j+=1
                else:
                    e=nums1[i]
                    i+=1
            elif i < n:
                e=nums1[i]
                i+=1
            else:
                e=nums2[j]
                j+=1
        if (n+m)%2 != 0:
            return float(e)
        else:
            median = float(e) + float(prev)
            return median / 2.0
nums1 = [1, 2, 7]
nums2 = [3, 4, 5, 8]
solution = Solution()
median = solution.findMedianSortedArrays(nums1, nums2)
print(median)
