class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=sorted(nums)
        ans=[]
        for i in range(len(n)):
            if i==0 or n[i]!=n[i-1]:
                target=n[i]*-1
                l,r=i+1,len(n)-1
                while l<r:
                    if n[l]+n[r]==target:
                        while l<len(n)-1 and n[l]==n[l+1]:
                            l+=1
                        while r<len(n)-1 and n[r]==n[r-1]:
                            r-=1
                        ans.append([n[i],n[l],n[r]])
                        l+=1
                        r-=1
                        
                        
                    elif n[l]+n[r]<target:
                        l+=1
                    else:
                        r-=1
        return ans
