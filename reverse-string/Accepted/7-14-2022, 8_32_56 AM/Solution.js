// https://leetcode.com/problems/reverse-string

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {

    for(let i =s.length-1;i>-1;i--){
       
        s.push(s[i]);
    
        
    };s.splice(0,s.length/2);
};