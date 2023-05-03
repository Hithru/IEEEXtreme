# Problem Number: 1491
# Problem Name: Find the Difference of Two Arrays
# Difficulty: Easy
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1_dict = {}
        nums2_dict = {}
        answer = [[],[]]
        for n in nums1:
            nums1_dict[n] = True
        for n in nums2:
            if n not in nums1_dict:
                answer[1].append(n)
            nums2_dict[n] = True

        for n in nums1:
            if n not in nums2_dict:
                answer[0].append(n)
        return [list(set(answer[0])),list(set(answer[1]))]