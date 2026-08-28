class Solution:
    def countSubstrings(self, s: str) -> int:
        is_palin = [[i == j for j in range(len(s))] for i in range(len(s))]
        substr = len(s)
        for i in range(2, len(s) + 1):
            for j in range(len(s) - i + 1):
                st, end = j, j+i-1
                if s[st] == s[end]:
                    if i == 2 or is_palin[st + 1][end - 1]:
                        is_palin[st][end] = True
                        substr += 1
        return substr
        