class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c for c in s if c.isalnum()).lower()
        
        def twoPointer(s1: str, s2: str):
            if s1 == s2:
                return True
            else:
                return False

        first = 0
        last = len(clean_s) - 1
        while True:
            if first >= last:
                return True
            if twoPointer(clean_s[first], clean_s[last]):
                first += 1
                last -= 1
            else:
                return False
