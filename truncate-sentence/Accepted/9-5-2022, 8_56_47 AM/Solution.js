// https://leetcode.com/problems/truncate-sentence

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    let z = s.split(" ");
    x=z.splice(0,k);
    return x.join(" ")
    
    
    
    
};