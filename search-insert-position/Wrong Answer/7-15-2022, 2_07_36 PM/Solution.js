// https://leetcode.com/problems/search-insert-position

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    for (let i of nums){
        if (target>i){
            return nums[i]-1;
            
            }
    }
    
};