from typing import List


class Solution(object):
    def removeDuplicatesWithSet(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result1 = s.removeDuplicatesWithSet(nums1)
    result2 = s.removeDuplicates(nums2)
    print(nums1)
    print(result1)
    print(nums2[:result1])
    print(result2)
