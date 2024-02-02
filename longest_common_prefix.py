# find longest common prefix of the first two words, store that to common variable
# find longest common prefix of the next word and the string in common variable,
# update common variable
# repeat above then return result


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]

        for string in strs[1:]:
            char_ind = 0
            common_temp = ''
            while char_ind < min(len(common), len(string)):
                if common[char_ind] == string[char_ind]:
                    common_temp += common[char_ind]
                    char_ind += 1
                else:
                    break
            common = common_temp
            if common == '':
                break
        return common
