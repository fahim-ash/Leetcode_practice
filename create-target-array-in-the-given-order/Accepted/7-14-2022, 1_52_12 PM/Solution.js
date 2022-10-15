// https://leetcode.com/problems/create-target-array-in-the-given-order

/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    let list=[];
    for (let i =0;i<nums.length;i++){
        list.splice(index[i],0,nums[i]);
        
        
    }return list;
    
};