class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        values = list(freq.values())
        if len(values) == len(set(values)):
            return True
        return False
         

        