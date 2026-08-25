class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const m={}
        const ans=[]
        for(let s of strs){
            const c=new Array(26).fill(0)
            for(let i=0;i<s.length;i++){
                c[s.charCodeAt(i)-"a".charCodeAt(0)]++
            }
            if(!m[c]) m[c]=[];
            m[c].push(s)
        }
        for(let i in m){
            ans.push(m[i])
        }
        return ans
    }
}
