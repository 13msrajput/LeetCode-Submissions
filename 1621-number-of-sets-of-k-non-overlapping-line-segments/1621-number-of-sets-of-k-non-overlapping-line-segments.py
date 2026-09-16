class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of ways for current number of segments
        # using points 0..i
        prev = [1] * n   # 0 segments

        for _ in range(k):
            curr = [0] * n
            prefix = 0

            for i in range(1, n):
                # Sum of prev[0 .. i-1]
                prefix = (prefix + prev[i - 1]) % MOD

                # Either:
                # 1. don't use i as right endpoint
                # 2. make a segment ending at i
                curr[i] = (curr[i - 1] + prefix) % MOD

            prev = curr

        return prev[n - 1]