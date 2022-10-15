// https://leetcode.com/problems/two-sum

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let s={};

    for (let i of nums){
        let curr=target-i;
        if (curr in s){
            if (curr==i){
                return ([nums.indexOf(curr),nums.indexOf(i)+1])
            }else{
            return([nums.indexOf(curr),nums.indexOf(i)]);}

        }else{
            s[i]=i;
        }

    }
    
};