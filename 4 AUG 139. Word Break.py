class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, memo)
    
    def dfs(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        if s in wordSet:
            return True
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordSet and self.dfs(s[i:], wordSet, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False
