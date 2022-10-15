// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    const hay=haystack.split("")
    
    let count=0;
    for (let i in hay)
        for (let j in hay)
            
            if (hay.slice(i,j).join("")==needle){
                return i
                
            }
    return -1
    
};