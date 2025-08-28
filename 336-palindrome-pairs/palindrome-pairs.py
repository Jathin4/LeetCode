class Solution:
    def palindromePairs(self, words):
        word_dict = {word[::-1]: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            n = len(word)
            
            for j in range(n + 1):
                prefix, suffix = word[:j], word[j:]
                
                # Case 1: prefix is palindrome → check reversed suffix
                if prefix == prefix[::-1] and suffix in word_dict and word_dict[suffix] != i:
                    res.append([word_dict[suffix], i])
                
                # Case 2: suffix is palindrome → check reversed prefix
                if j != n and suffix == suffix[::-1] and prefix in word_dict and word_dict[prefix] != i:
                    res.append([i, word_dict[prefix]])
        
        return res
