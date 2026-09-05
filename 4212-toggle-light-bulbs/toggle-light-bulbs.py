class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d={}
        for bulb in bulbs:
            if bulb in d:
                d[bulb] =not d[bulb]
            else:
                d[bulb] = True
        result = []
        for bulb in d:
            if d[bulb]:
                result.append(bulb)
        return sorted(result)






        
        