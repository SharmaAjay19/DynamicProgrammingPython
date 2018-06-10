class Solution:
    def threeSum(self, nums):
        nums.sort()
        size = len(nums)
        results = []
        for i in range(size-2):
            sumval = -1*nums[i]
            l = i+1
            r = size-1
            while l<r:
                if (nums[l]+nums[r]) == sumval:
                    if [nums[i], nums[l], nums[r]] not in results:
                        results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r += -1
                elif nums[l]+nums[r]>sumval:
                    r += -1
                else:
                    l += 1
        return results
sol = Solution()
inp = list(map(int, input().split(",")))
print(sol.threeSum(inp))