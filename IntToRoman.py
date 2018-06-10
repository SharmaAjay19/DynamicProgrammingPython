class Solution:
    def intToRoman(self, num):
        symbols = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        p = len(symbols)-1
        result = []
        while (p>0) and (num%symbols[p][0]>0):
            #print("num:", num, "div:", symbols[p], "p:", p)
            if int(num/symbols[p][0])>0:
                q = int(num/symbols[p][0])
                num = num%symbols[p][0]
                result += [symbols[p][1] for i in range(q)]
            p += -1
            #print("num:", num, "div:", symbols[p], "p:", p, "r:", num%symbols[p])
        if int(num/symbols[p][0])>0:
            q = int(num/symbols[p][0])
            result += [symbols[p][1] for i in range(q)]
        return ''.join(result)
sol = Solution()
inp = int(input())
print(sol.intToRoman(inp))