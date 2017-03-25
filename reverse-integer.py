class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        neg = 1
        if x < 0:
            neg, x = -1, -x

        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x / 10

        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse
