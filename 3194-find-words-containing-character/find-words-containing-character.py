class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        w = []
        for ele in range(len(words)):
            if x in words[ele]:
                w.append(ele)
        return w
