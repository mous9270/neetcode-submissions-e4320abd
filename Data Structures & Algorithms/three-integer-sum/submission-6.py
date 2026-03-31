class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=sorted(nums)
        ans=[]
        for i in range(len(n)):
            if i==0 or n[i]!=n[i-1]:
                t=n[i]*-1
                l,r=i+1, len(n)-1
                while l<r:
                    while l<r and n[l]==n[l+1]:
                        l+=1
                    while l<r and n[r]==n[r-1]:
                        r-=1
                    if n[l]+n[r]==t:
                        ans.append([n[i], n[l], n[r]])
                        l+=1
                        r-=1
                    elif n[l]+n[r]<t:
                        l+=1
                    else:
                        r-=1
        return ans

