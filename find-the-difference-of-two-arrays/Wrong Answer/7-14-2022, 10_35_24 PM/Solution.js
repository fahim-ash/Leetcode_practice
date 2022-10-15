// https://leetcode.com/problems/find-the-difference-of-two-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    for (let i of nums1){
        for(let j of nums2){
            if (i==j){
                nums1.splice(nums1.indexOf(j),1);
                nums2.splice(nums2.indexOf(j),1);
            }
        }
    }return [nums1,nums2]
    
};