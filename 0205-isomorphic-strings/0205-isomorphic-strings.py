class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        if len(s) != len(t):
            return False

        for i, c in enumerate(s):
            if c in s_to_t:
                if t[i] != s_to_t[c]:
                    return False
            else:
                s_to_t[c] = t[i]

            if t[i] in t_to_s:
                if c != t_to_s[t[i]]:
                    return False
            else:
                t_to_s[t[i]] = c

        return True
