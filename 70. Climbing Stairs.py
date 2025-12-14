class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return (1)
        elif n == 2 :
            return 2
        else:
            check = [0] * (n+1)
            check[1] = 1
            check[2] = 2
            for i in range (3,len(check)):
                check[i] = check[i-1] + check[i-2]
        return check[n]