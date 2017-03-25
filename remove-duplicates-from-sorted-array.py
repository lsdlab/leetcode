class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0 or n == 1:
            return n
        j = 0
        for i in range(1, n):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1
