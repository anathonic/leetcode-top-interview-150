from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        j = 1
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                counter += 1
            else:
                counter = 1
            if counter <= 2:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    s = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3]
    j = s.removeDuplicates(nums)
    print(nums[:j])
