class Solution:
    def getParenthesis(self, curr, open, close, n):
        if close==n:
            return [curr]
        results = []
        if open>close:
            results += self.getParenthesis(curr + ")", open, close+1, n)
        if open<n:
            results += self.getParenthesis(curr + "(", open+1, close, n)
        return results
    def generateParenthesis(self, n):
        return self.getParenthesis("", 0, 0, n)
sol = Solution()
inp = int(input())
print(sol.generateParenthesis(inp))