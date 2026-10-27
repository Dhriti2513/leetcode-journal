class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            if i == 0:
                # Top row is entirely free
                grid.append('.' * n)
            else:
                # Subsequent rows are blocked except for the last column
                grid.append('#' * (n - 1) + '.')
        return grid