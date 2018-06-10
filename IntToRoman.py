class Solution:
    def intToRoman(self, num):
        refdict = dict([(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M')])
        symbols = [1, 5, 10, 50, 100, 500, 1000]
        p = len(symbols)-1
        result = []
        while num%symbols[p]>0:
            if int(num/symbols[p])>0:
                q = int(num/symbols[p])
                num = num%symbols[p]
                result += [refdict[symbols[p]] for i in range(q)]
                p += -1
            elif p>0 and num>=(4*(symbols[p]-symbols[p-1])/5)

sol = Solution()
print(sol.intToRoman(2))