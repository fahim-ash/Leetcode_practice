// https://leetcode.com/problems/build-array-from-permutation

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    let list=[];
    for (let i of nums){
        list.push(nums[i]);
        
    }; return list;
    
};