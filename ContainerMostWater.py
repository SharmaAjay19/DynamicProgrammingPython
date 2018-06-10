class Solution:
    def maxArea(self, height):
        size = len(height)
        l = 0; r = size-1; area = 0
        while l<r:
            area = max([area, min([height[l], height[r]])*(r-l)])
            if height[l]<height[r]:
                l += 1
            else:
                r += -1
        return area
inp = list(map(int, input().split(",")))
sol = Solution()
print(sol.maxArea(inp))