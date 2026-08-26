class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const m={}
        for(let i=0;i<nums.length;i++){
            if(nums[i] in m){
                return true
            }
            m[nums[i]]=0
        }
        return false
    }
}
