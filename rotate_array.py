from typing import List


class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 3
    s.rotate(nums, k)
    print(nums)