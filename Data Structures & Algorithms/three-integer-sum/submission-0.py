class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # T.C. O(n3), S.C. O(m)
        # result = set()
        # for i in range(0,len(nums) - 2):
        #     for j in range(i+1,len(nums) - 1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 result.add(triplet)
        # return [list(ans) for ans in result]

        # T.C. = O(n2), S.C. O(1)
        result = []
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
        