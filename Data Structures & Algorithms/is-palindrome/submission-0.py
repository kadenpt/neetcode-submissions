class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c for c in s if c.isalnum()).lower()
        if clean_s == clean_s[::-1]:
            return True

        return False
