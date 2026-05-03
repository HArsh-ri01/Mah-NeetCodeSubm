class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, r = 0, len(s) -1

        while i < r:
            while i <r and not self.alphanum(s[i]):
                i += 1 
            while r > i and not self.alphanum(s[r]):
                r -= 1
            if s[i].lower() != s[r].lower():
                return False
            i, r = i + 1, r - 1
        return True

    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')or 
         ord('a') <= ord(c) <= ord('z')or
         ord('0') <=ord(c) <= ord('9')) 