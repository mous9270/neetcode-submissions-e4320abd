class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length!==t.length){
            return false
        }
        const ms={}
        const mt={}
        for(let i=0;i<s.length;i++){
            ms[s[i]]=(ms[s[i]] || 0)+1
            mt[t[i]]=(mt[t[i]] || 0)+1
        }
        for(const i in ms){
            if(ms[i]!==mt[i]){
                return false
            }
        }
        return true

    }
}
