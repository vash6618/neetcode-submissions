class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while(n):
            if n%2:
                cnt += 1
            n = n//2
        return cnt
        