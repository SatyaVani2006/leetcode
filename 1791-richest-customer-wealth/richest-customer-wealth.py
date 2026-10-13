class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumWealth = 0

        for row in accounts:
            total = 0
            for value in row:
                total = total + value

            if total > maximumWealth:
                maximumWealth = total

        return maximumWealth