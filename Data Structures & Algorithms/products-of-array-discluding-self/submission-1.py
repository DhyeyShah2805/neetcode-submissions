class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            ans = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    ans *= nums[j]
            result.append(ans)
        return result