class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
