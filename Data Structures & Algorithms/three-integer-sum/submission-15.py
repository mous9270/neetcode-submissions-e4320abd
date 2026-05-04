class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=sorted(nums)
        for i in range(len(n)):
            target=n[i]*-1
            l,r=i+1,len(n)-1
            if i==0 or n[i]!=n[i-1]: 
                while l<r:
                    
                    if n[l]+n[r]==target:
                        while  l<r and n[l]==n[l+1]:
                            l+=1
                        while  l<r and n[r]==n[r-1]:
                            r-=1
                        ans.append([n[i],n[l],n[r]])
                        l+=1
                        r-=1
                    elif n[l]+n[r]<target:
                        l+=1
                    else:
                        r-=1
                   
        return ans