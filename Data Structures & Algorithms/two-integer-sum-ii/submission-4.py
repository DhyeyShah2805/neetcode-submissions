class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

        # T.C. = O(n), S.C. = O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1]