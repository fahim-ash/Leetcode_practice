// https://leetcode.com/problems/reverse-words-in-a-string

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let word=s.split(" ");
    let new1=[];
    for(let i =word.length-1;i>-1;i--){
        if (word[i]!=""){
        new1.push(word[i])};
        
        
        
    };return new1.join(" ");
};