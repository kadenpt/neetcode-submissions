class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)

        for i in range(len(s) - 1):
            current = s[i]
            
            for r in range(i + 1, len(s)):
                current += s[r]
                if self.isPalindrome(current):
                    res += 1
        
        return res
                
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True