class Solution:
    def plusOne(self, digits: list[int]):
        i = len(digits) - 1
        while True:
            digits[i] = digits[i] + 1
            if i == 0 and digits[i] == 10 :
                digits[i] = 0
                digits.insert(0,1)
                break
            elif digits[i] == 10:
                digits[i] = 0
                i = i - 1
                continue
            else:
                return digits
        return digits
        