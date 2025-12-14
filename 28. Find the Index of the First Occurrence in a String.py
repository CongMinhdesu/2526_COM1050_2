class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = 0
        i = 0
        check = 1
        while True:
            if i > len(haystack)-1:
                break
            if haystack[i] == needle[k]:
                k = k + 1
                i = i + 1
                if k > len(needle)-1:
                    return i -1 - len(needle) + 1
            else:
                k = 0
                i = check
                check = check + 1
        return -1 
        