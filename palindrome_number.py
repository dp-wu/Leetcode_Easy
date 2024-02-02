# use two pointers one point to the left and one point to the right
class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = str(x)
        first = 0
        last = len(digits) - 1
        while first < last:
            if digits[first] != digits[last]:
                return False
            first += 1
            last -= 1
        return True
