# Problem Number: 4
# Problem Name: Median Of Two Sorted Arrays
# Difficulty: Hard

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        middle = (len(nums1) + len(nums2)) // 2
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        if (len(nums1) + len(nums2)) % 2 == 1:
            middle += 1

            i = 0
            j = 0

            for k in range(middle):
                if nums1[i] < nums2[j]:
                    i += 1
                    if k == middle - 1:
                        return nums1[i - 1]
                else:
                    j += 1

                    if k == middle - 1:
                        return nums2[j - 1]
        else:

            i = 0
            j = 0
            num1 = 0
            num2 = 0

            for k in range(middle + 1):
                if nums1[i] < nums2[j]:
                    i += 1
                    if k == middle - 1:
                        num1 = nums1[i - 1]
                    if k == middle:
                        num2 = nums1[i - 1]
                else:
                    j += 1

                    if k == middle - 1:
                        num1 = nums2[j - 1]
                    if k == middle:
                        num2 = nums2[j - 1]
            return (num1 + num2) / 2
