# use stack to store left parenthesis
# pop from the top of the stack if there is a matching right parenthesis
# return False if stack is not empty


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        if s[0] in pairs:
            stack = [s[0]]
        else:
            return False

        for p in s[1:]:
            if p in pairs:
                stack.append(p)
            else:
                if stack and pairs[stack[-1]] == p:
                    stack.pop(-1)
                else:
                    return False

        if stack:
            return False
        else:
            return True
