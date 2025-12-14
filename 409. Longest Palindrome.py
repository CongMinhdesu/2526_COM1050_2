class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in range (len(s)):
                dic[s[i]]=0
        for i in range (len(s)):
                dic[s[i]] += 1
        k = 0
        p = 0
        if len(s) == 1:
            return 1
        else:
            for i in dic.values():
                if i % 2 == 0:
                    k = k + i
                elif i % 2 != 0 and i != 1:
                    k = k + i - 1
                    p = 1
                else: 
                    p = 1
            return k + p