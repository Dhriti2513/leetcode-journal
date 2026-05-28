class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()
        
        default_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[default_idx]):
                default_idx = i
                
        root.best_idx = default_idx
        
        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                if curr.best_idx == -1:
                    curr.best_idx = i
                else:
                    if len(word) < len(wordsContainer[curr.best_idx]):
                        curr.best_idx = i
                        
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_idx)
            
        return ans
        
        
