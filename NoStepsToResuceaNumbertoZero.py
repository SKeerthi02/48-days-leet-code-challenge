class Solution:
    def numberOfSteps (self, num: int) -> int:
        num = bin(num)[2:]
        count = 0
        for n in num:
            if n == "1":
                count += 2
            else:
                count += 1
        return count -1
