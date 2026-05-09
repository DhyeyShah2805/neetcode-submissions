class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # T.C. O(n2). SC O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return sorted([i, seen[complement]])
            seen[nums[i]] = i
