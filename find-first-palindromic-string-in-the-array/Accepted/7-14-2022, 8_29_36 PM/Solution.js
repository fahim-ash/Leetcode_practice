// https://leetcode.com/problems/find-first-palindromic-string-in-the-array

/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    let count=0;
    for(let i of words){
        let z=i.split("");
        let rev= z.reverse();
        let again=rev.join("");
        if (again==i){
            return i;
            count++;
            break;
            };
            };
    if (count ==0){
        return "";
    };
    };