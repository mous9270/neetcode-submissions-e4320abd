class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=defaultdict(list)
        for i in strs:
            c=[0 for i in range(ord('z')-ord('a')+1)]
            for j in i:
                c[ord(j)-ord('a')]+=1
            m[tuple(c)].append(i)
        return list(m.values())
        