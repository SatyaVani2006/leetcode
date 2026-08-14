class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels=dict()
        consonants=dict()
        for i in s:
            if i in "aeiou":
                if i in vowels:
                    vowels[i]+=1
                else:
                    vowels[i]=1
            else:
                if i in consonants:
                    consonants[i]+=1
                else:
                    consonants[i]=1
        vowels_max=max(vowels.values(),default=0)
        conso_max=max(consonants.values(),default=0)
        return vowels_max+conso_max
            
       

        