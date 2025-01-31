from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 2, 3, 3, 2, 3, 2, 3]
    val = 3
    result = s.removeElement(nums, val)
    print(nums[:result])
    print(result)