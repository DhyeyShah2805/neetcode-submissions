class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # T.C. O(n2), S.C. O(1)
        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         width = j-i
        #         maxArea = max(maxArea, min(heights[i],heights[j]) * width)
        # return maxArea

        # T.C. O(n), S.C. O(1)
        left, right = 0, len(heights) - 1
        maxArea = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            currentArea = width * height

            maxArea = max(maxArea, currentArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea




