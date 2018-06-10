class Solution:
    def threeSum(self, nums):
        #nums.sort()
        size = len(nums)
        results = []
        for i in range(size-1):
            hashdict = {}
            for j in range(i+1, size):
                if -(nums[i]+nums[j]) in hashdict:
                    hashdict.pop(-(nums[i]+nums[j]), None)
                    results.append((nums[i], nums[j], -(nums[i]+nums[j])))
                else:
                    hashdict[nums[j]] = 1
        results = list(set(results))
        return [list(x) for x in results]
sol = Solution()
inp = list(map(int, input().split(",")))
print(sol.threeSum(inp))