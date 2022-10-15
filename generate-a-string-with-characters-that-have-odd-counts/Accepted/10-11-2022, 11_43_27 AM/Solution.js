// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts

/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    
    let word="";
    if (n%2!=0){
        for (let i=0;i<n;i++){
            word+="a";
        }
    return word;   
    }else {
        for (let i=0;i<n-1;i++){
            word+="a";
        
    }word=word+"b";
        return word;
    }
};