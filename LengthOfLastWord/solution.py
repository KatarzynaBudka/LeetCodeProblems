class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        last_word_len = len(words[-1])
        i = -1
        while last_word_len<1:
            i-=1
            last_word_len = len(words[i])
        return last_word_len
    