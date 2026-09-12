class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        sorted_intervals = sorted(
            (intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)
        )

        L = [interval[0] for interval in sorted_intervals]

        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l_i, r_i, w_i, idx_i = sorted_intervals[i]
            j = bisect_right(L, r_i)

            for c in range(1, 5):
                opt1_score, opt1_indices = dp[i + 1][c]

                sub_score, sub_indices = dp[j][c - 1]
                opt2_score = w_i + sub_score
                opt2_indices = tuple(sorted((idx_i,) + sub_indices))

                key1 = (-opt1_score, opt1_indices)
                key2 = (-opt2_score, opt2_indices)

                if key2 < key1:
                    dp[i][c] = (opt2_score, opt2_indices)
                else:
                    dp[i][c] = (opt1_score, opt1_indices)

        return list(dp[0][4][1])