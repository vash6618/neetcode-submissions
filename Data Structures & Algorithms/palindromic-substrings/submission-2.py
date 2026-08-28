class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palins(st_ind, length, s):
            substr = 0
            while(length <= len(s)):
                st = st_ind - length//2
                end = st_ind + length//2 if length % 2 else st_ind + length//2 - 1
                if st < 0 or end >= len(s) or s[st] != s[end]:
                    break
                substr += 1
                length += 2
            return substr
        ans = len(s)
        for j in range(1, len(s)):
            ans += count_palins(j, 2, s)
            ans += count_palins(j, 3, s)

        return ans
        