// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    let w1=word1.join("");
    let w2= word2.join("");
    return w1==w2;
    
};