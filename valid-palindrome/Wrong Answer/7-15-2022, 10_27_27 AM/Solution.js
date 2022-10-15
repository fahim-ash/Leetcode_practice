// https://leetcode.com/problems/valid-palindrome

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let list=[];
    for (let i of s){
        if (i!="," || i!=" "||i!=":"){
            list.push(i);
        };
    };
    let z= list.reverse();
    if (z==list){
        return true;
    }else{
        false;
    };
    
};