class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        st = 0
        e = 0

        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1
        for i in range(len(s)):
            l1,r1 = expand(i,i)
            l2,r2 = expand(i,i+1)
            if r1 - l1 > e - st:
                st = l1
                e = r1
            if r2 - l2 > e - st:
                st = l2
                e = r2
        return s[st:e+1] 