// https://leetcode.com/problems/find-greatest-common-divisor-of-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    let max=1;
    let list=nums.sort((a,b)=>a-b);
    for (let i =0;i<=list[list.length-1];i++){
        if (list[0]%i==0 && list[list.length-1]%i==0){
            max=i;
        };

    };return max;
    
};