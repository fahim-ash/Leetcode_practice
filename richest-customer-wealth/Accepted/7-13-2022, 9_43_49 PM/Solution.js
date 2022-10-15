// https://leetcode.com/problems/richest-customer-wealth

/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max=0;
    for (let i of accounts){
        let count=0;
        for (let j of i){
            count=count+j;
            
            
        }if (count>max){
            max=count;
             
             }
        
    }return max;
    
    
};