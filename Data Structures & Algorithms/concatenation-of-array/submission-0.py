class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # make new array and process each elemnt and add copy to new array. Then return str + new_str
        n = len(nums)
        ans = [0] * (2*n)
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans