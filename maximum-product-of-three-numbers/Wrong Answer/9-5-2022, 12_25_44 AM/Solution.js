// https://leetcode.com/problems/maximum-product-of-three-numbers

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    let count=1;
    for (let i of nums){
        count=count*i;
        
        
    };
    return count;
    
};