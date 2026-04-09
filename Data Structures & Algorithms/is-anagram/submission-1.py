class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True
