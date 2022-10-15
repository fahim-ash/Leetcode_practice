// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    var count = 0
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] >= nums[i + 1]) {
            count += nums[i] - nums[i+1] + 1
            nums[i+1] = nums[i] + 1
        }
    }
    return count

};