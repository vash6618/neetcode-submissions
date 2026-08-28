class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palins(l, r):
            substr_cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                substr_cnt += 1
            return substr_cnt
        ans = 0
        for j in range(len(s)):
            ans += count_palins(j, j)
            ans += count_palins(j, j + 1)

        return ans
        