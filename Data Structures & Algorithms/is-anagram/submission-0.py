class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values_s = dict()
        for char in s:
            if char in values_s:
                values_s[char] += 1
            else:
                values_s[char] = 0

        values_t = dict()
        for char in t:
            if char in values_t:
                values_t[char] += 1
            else:
                values_t[char] = 0
        if values_s == values_t:
            return True
        return False

        
            


        
        