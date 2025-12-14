class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        l = 0
        r = 0
        ans = 0
        if len(s) == 0 or len(g) == 0:
            return 0
        else:
            while True:
                if s[r] >= g[l]:
                    ans = ans + 1
                    r = r + 1
                    l = l + 1
                elif s[r] < g[l]:
                    r = r + 1
                if r > len(s) - 1 or l > len(g)-1:
                    break
            return ans
            
