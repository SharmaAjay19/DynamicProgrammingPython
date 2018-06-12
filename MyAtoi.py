class Solution:
    def isDigit(self, ch):
        if ord(ch)>=48 and ord(ch)<=57:
            return true
        return false
    def myAtoi(self, str):
        sign = 0
        nums = ""
        i = 0
        size = len(str)
        while str[i]==" ":
            i += 1
        if str[i]=="-":
            sign = 1
        elif str[i]=="+":
            sign = 0
        elif self.isDigit(str[i]):
            