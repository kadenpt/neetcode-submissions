class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        def dfs(left, right, deleted):
            if left > right:
                return True

            if s[left] != s[right]:
                if not deleted:
                    return dfs(left + 1, right, True) or dfs(left, right - 1, True)
                else:
                    return False
            
            return dfs(left + 1, right - 1, deleted)
        
        return dfs(l, r, False)