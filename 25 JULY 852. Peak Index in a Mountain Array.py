class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            if mid==0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low=mid+1
            elif mid==n-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    high=mid-1
            else:
                if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                    return mid
                elif nums[mid]<nums[mid+1]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
