class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = whether s[l:r+1] is a palindrome
        # bytearray uses much less memory than Python bool objects.
        pal = [bytearray(n) for _ in range(n)]

        # Length 1 palindromes
        for i in range(n):
            pal[i][i] = 1

        # Length >= 2
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (
                    length == 2 or pal[l + 1][r - 1]
                ):
                    pal[l][r] = 1

        # dp[i] = max number of valid palindromes in s[:i]
        dp = [0] * (n + 1)

        for r in range(n):
            # Don't use s[r] in a palindrome ending at r
            dp[r + 1] = dp[r]

            # Try every palindrome ending at r
            for l in range(r - k + 2):
                if pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]