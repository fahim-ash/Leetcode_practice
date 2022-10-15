// https://leetcode.com/problems/longest-common-subsequence

/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    let count =0;
    for(let i in text1){
        for(let j in text2){
            if (i==j){
                text2.substr(j);
                count++;
                
                };
        };
    };
        return count;
    };
    