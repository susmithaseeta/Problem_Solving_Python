
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

            if sign * num > 2**31 - 1:
                return 2**31 - 1
            if sign * num < -2**31:
                return -2**31

        return sign * num
