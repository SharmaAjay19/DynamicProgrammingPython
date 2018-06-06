class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        isPalin = [[0 for i in range(size)] for j in range(size)]
        maxl = 1; maxind = (0, 1)
        for i in range(size):
            isPalin[i][i] = 1
        for i in range(size):
            ind = size-i-1
            for j in range(ind+1, size):
                if (s[ind]==s[j]) and (((j-ind)==1) or isPalin[ind+1][j-1]):
                    isPalin[ind][j] = 1
            for j in range(0, size-ind-1):
                if isPalin[ind][size-j-1] and ((size-j-ind)>=maxl):
                    maxl = size-j-ind
                    maxind = (ind, size-j)
                    break
        return s[maxind[0]:maxind[1]]
inp = input()
sol = Solution()
print(sol.longestPalindrome(inp))