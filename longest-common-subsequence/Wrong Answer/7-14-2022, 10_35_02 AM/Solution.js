// https://leetcode.com/problems/longest-common-subsequence

/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    let count =0;
    let t1=text1.split("");
    let t2=text2.split("");
    for (let i of t1){
        for (let j of t2){
            if (i==j)
            count++;
        }
    }return count;
   
    


};
    