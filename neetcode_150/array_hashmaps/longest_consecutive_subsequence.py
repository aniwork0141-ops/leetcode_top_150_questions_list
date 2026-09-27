class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = sorted(set(nums))
        count=1
        max=1
        for i in range(1,len(nums)):
            if not (nums[i] - (nums[i-1] + 1) == 0):
                count=1
            else:
                count+=1
                if count>max:
                    max = count
        return max
