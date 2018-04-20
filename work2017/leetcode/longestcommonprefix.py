class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        head = sorted(strs)[0]
        for i in range(len(strs)):
            if head != strs[i][0: len(head)]:
                


