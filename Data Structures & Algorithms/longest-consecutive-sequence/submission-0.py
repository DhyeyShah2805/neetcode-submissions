class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        counter = 1
        maxLength = 1
        for i in range(len(nums) - 1):
            if nums[i] - nums[i+1] == 0:
                continue
            if nums[i] - nums[i+1] == -1:
                counter+=1
            else:
                counter = 1
            maxLength = max(maxLength, counter)
        return maxLength
        
        
        
        # num_set = set(nums)
        # longest = 0
        # for num in num_set:

        #     if num - 1 not in num_set:
        #         length = 1
        #         while num+length in num_set:
        #             length +=1
        #         longest = max(longest,length)
        # return longest
