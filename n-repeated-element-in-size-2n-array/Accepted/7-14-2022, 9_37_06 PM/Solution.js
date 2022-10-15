// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    let list=[];
    for (let i of nums){
        if (list[i]==i){
            return i;
        }else{
            list[i]=i;
        }
        
    }
    
};