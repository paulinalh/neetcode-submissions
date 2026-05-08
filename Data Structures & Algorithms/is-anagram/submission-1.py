class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):
            if s[i] in hashmapS:
                hashmapS[s[i]] = hashmapS[s[i]] + 1
            else:
                hashmapS[s[i]] = 1

            if t[i] in hashmapT:
                hashmapT[t[i]] = hashmapT[t[i]] + 1
            else:
                hashmapT[t[i]] = 1
        

 
        for c in hashmapS:
            if hashmapS.get(c, 0) != hashmapT.get(c, 0):
                return False
        
        return True