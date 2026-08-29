class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26 #start at 0 letters of all alphabet present
            
            for letter in word:
                count[ord(letter) - ord('a')] += 1 #find out which letters and how many letters present
            
            anagrams[tuple(count)].append(word) #add words with same properties to list

        return list(anagrams.values())