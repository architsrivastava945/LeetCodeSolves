class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num > 9:
            sum = 0
            while num > 0:
                i = num % 10
                num = num // 10
                sum += i
            num = sum

        return num
