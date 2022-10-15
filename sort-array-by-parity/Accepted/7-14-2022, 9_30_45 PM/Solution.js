// https://leetcode.com/problems/sort-array-by-parity

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    let list=[];
    for (let i of nums){
        if (i%2){
        list.push(i)}
        else{
            list.unshift(i);
        }
     
    }return list;

    
};