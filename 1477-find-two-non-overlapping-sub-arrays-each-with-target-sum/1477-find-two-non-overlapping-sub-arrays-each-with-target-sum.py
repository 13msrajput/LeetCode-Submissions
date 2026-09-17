class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = shortest valid subarray in arr[0:i+1]
        best = [INF] * n

        ans = INF
        left = 0
        curr_sum = 0
        min_len = INF

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window until sum <= target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray [left, right] with sum == target
            if curr_sum == target:
                length = right - left + 1

                # Need another subarray completely before `left`
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                # Update shortest valid subarray seen so far
                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if ans == INF else ans