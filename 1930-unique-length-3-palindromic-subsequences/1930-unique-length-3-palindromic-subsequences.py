class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        res = set()
        char_map = {}

        for i, c in enumerate(s):
            if c not in char_map:
                char_map[c] = [i, i]
            else:
                char_map[c][1] = i
        
        for c, (start, end) in char_map.items():
            if end - start >= 2:  
                for i in range(start + 1, end):
                    res.add(c + s[i] + c)  
        
        return len(res)