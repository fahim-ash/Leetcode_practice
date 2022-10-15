// https://leetcode.com/problems/concatenation-of-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    list=[]
    for (let i=0;i<nums.length;i++){
        list.push(nums[i]);
    }
    for (let i=0;i<nums.length;i++){
        list.push(nums[i]);
};return list;
};