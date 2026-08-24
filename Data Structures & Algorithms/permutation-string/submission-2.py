class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m1 = {}
        for ch in s1:
            m1[ch] = m1.get(ch, 0) + 1

        need = len(m1)      # distinct chars required
        have = 0            # distinct chars currently at exact count
        m2 = {}
        l = 0

        for r in range(len(s2)):
            c = s2[r]

            # char not in s1 at all -> no valid window can span it, hard reset
            if c not in m1:
                m2.clear()
                have = 0
                l = r + 1
                continue

            m2[c] = m2.get(c, 0) + 1
            if m2[c] == m1[c]:
                have += 1

            # too many of c -> shrink from left until it's legal again
            while m2[c] > m1[c]:
                left = s2[l]
                if m2[left] == m1[left]:
                    have -= 1
                m2[left] -= 1
                l += 1

            if have == need:
                return True

        return False

                
                    

        