# use python dicitonary to store roman numerals
# special cases such as IV, IX, XL, XC, CD, CM are computed by 
# subtracting the smaller value from the larger value

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        index = 0
        length = len(s)
        while index < length-1:
            if d[s[index]] < d[s[index+1]]:
                result += (d[s[index+1]] - d[s[index]])
                index += 2
            else:
                result += d[s[index]]
                index += 1
        if index == length-1:
            result += d[s[index]]
        return result