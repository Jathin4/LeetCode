class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        c = 0
        for i in words[left:right+1]:
            if i[0] in 'aeiou' and i[-1] in 'aeiou':
                c += 1
        return c
        