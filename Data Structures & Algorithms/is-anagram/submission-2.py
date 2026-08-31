class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        for char in t:
            hashmap[char] = hashmap.get(char, 0) - 1

        return all(count == 0 for count in hashmap.values())