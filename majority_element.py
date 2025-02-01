from typing import List


class Solution(object):
    def majorityElement(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 3]
    result = s.majorityElement(nums)
    print(result)