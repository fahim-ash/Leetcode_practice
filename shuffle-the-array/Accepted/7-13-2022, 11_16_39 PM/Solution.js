// https://leetcode.com/problems/shuffle-the-array

/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let list =[];
    for (let i=0;i<=nums.length-n-1;i++){
        list.push(nums[i]);
        list.push(nums[i+n]);
        
    }return list;
    
};