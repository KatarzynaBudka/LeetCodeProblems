class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        k = 0
        while i <len(s) and k<len(t):
            if s[i] == t[k]:
                i+=1
                k+=1
            else:
                k+=1
        is_subsequence = True if i==len(s) else False   
        return is_subsequence