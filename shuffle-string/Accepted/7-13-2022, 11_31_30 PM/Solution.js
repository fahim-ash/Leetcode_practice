// https://leetcode.com/problems/shuffle-string

/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let word=[];
    for (let i=0;i<s.length;i++){
        word[indices[i]]=s[i];

    };
     return word.join("");
    
    
};