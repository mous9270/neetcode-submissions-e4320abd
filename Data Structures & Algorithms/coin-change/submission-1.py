class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m={0:0}
        a=amount
        c=sorted(coins)

        for i in range(1, amount+1):
            for j in c:
                t=i-j
                if t<0:
                    break
                if t in m:
                    k=m[t]+1
                    if i not in m or m[i]>k:
                        m[i]=k
        return m[a] if a in m else -1