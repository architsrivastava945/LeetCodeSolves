class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)
        for str in strs:
            freq = [0]*26
            for s in str:
                freq[ord(s) - ord('a')] += 1
            key = ""
            for i in range(len(freq)):
                if freq[i] > 0:
                    key = key + f"{chr(i+ord('a'))}{freq[i]}"
            result[key].append(str)
        return list(result.values())