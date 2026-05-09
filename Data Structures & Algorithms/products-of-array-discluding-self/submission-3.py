class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # T.C. = O(n2), S.C. = O(1)
        # result = []
        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             ans *= nums[j]
        #     result.append(ans)
        # return result

        # T.C. = O(n), S.C. = O(n)
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result




