// https://leetcode.com/problems/count-items-matching-a-rule

/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let count =0;
    for (let i of items){
        for (let j of i ){
            console.log(j);
                if (j==ruleValue){
                    count ++;
                    
                }else if (ruleKey=="color"){
                if (j==ruleValue){
                    count ++;
                    
            }else if (ruleKey=="name"){
                if (j==ruleValue){
                    count ++;
        };
    };
    
};};};return count;};