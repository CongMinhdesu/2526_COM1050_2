class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0 :
            return False
        else:
            k = []
            for i in range (len(s)):
                if s[i] == '(':
                    k.append(')')
                elif s[i] == '[':
                    k.append(']')
                elif s[i] == '{':
                    k.append('}')


                if s[i] == ')':
                    if len(k) - 1 < 0:
                        return False
                    elif k[len(k)-1] == ')':
                        k.pop(len(k)-1)
                    else:
                        return False
                elif s[i] == '}':
                    if len(k) - 1 < 0:
                        return False
                    elif k[len(k)-1] == '}':
                        k.pop(len(k)-1)
                    else:
                        return False
                elif s[i] == ']':
                    if len(k) - 1 < 0:
                        return False
                    elif k[len(k)-1] == ']':
                        k.pop(len(k)-1)
                    else:
                        return False
            if len(k) != 0:
                return False
            return True