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
        const c = new Array(26).fill(0)
        for(let i=0;i<s.length;i++){
            c[s.charCodeAt(i)-"a".charCodeAt(0)]++;
            c[t.charCodeAt(i)-"a".charCodeAt(0)]--;
        }
        return c.every((i)=>i===0);
    }
}
