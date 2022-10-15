// https://leetcode.com/problems/count-items-matching-a-rule

/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let obj={"type":0,"color":1,"name":2};
    let key=obj[ruleKey];
    let count=0;
    for (let i of items){
        if (i[key]==ruleValue)
        count++;
    }return count;
    
    


};