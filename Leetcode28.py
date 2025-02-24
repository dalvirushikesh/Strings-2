# Time Complexity = O(m*n)
# Space Complexity = O (n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1
