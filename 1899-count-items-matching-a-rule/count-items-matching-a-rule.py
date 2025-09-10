class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        c = 0
        for i in items:
            if ruleKey == "color":
                if i[1] == ruleValue:
                    c += 1
            if ruleKey == "type":
                if i[0] == ruleValue:
                    c += 1
            if ruleKey == "name":
                if i[2] == ruleValue:
                    c += 1
        return c