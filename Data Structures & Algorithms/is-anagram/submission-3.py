class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values_s, values_t = dict(), dict()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in values_s:
                values_s[s[i]] += 1
            else:
                values_s[s[i]] = 0
            if t[i] in values_t:
                values_t[t[i]] += 1
            else:
                values_t[t[i]] = 0

        if values_s == values_t:
            return True
        return False

        
            


        
        