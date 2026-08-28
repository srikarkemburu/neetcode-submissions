class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif set(s) != set(t):
            return False
        else:
            for c, k in zip(sorted(s), sorted(t)):
                if s.count(c) != t.count(k):
                    return False
            return True



