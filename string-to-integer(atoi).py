class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0
        i = 0
        sign = 1
        result = 0
        length = len(str)
        MaxInt = (1 << 31) - 1
        MinInt = -(1 << 31)
        if str[0] == '+':
            i += 1
        elif str[0] == '-':
            i += 1
            sign = -1

        for i in range(i, length):
            if str[i] < '0' or str[i] > '9':
                break
            result = result * 10 + int(str[i])
            if result > MaxInt:
                break
        result *= sign
        if result >= MaxInt:
            return MaxInt
        if result <= MinInt:
            return MinInt
        return result
