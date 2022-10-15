// https://leetcode.com/problems/two-sum

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {}

    for (let index = 0; index < nums.length; index++) {
        const element = nums[index];
        let remaining = target - element
        if (remaining in map) { 
            return [map[remaining], index]
        }
		
         map[element] = index

    }
};