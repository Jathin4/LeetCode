class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a = set(sentence)
        if len(a)>= 26:
            return True
        else:
            return False
        