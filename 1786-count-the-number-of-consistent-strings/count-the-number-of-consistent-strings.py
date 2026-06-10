class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        return sum(set(word) <= allowed for word in words)