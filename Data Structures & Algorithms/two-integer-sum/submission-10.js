class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const m={};
        for(let i=0;i<nums.length;i++){
            if(target-nums[i] in m){
                return [m[target-nums[i]], i]
            }
            m[nums[i]]=i;
        }
    }
}
