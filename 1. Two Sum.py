class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()
        for i,num in enumerate(nums):
            if target-num in mapping.keys():
                return list((mapping[target-num], i))
            else:
                mapping[num] = i
        return list()