class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i=0
        j=len(nums)-1
        while(i<j):
            if nums[i]+nums[j]==target:
                return i,j
            if nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
