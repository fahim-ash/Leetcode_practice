// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let list=nums.sort((a,b)=>b-a);
    let res=(list[0]-1)*(list[1]-1);
    return res;
    
    
};