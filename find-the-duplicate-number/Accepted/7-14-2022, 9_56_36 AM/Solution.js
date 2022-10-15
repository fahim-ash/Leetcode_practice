// https://leetcode.com/problems/find-the-duplicate-number

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let list=[];
    for (let i of nums){
      if(list[i]==i){
          return i;
         
      }else{
          list[i]=i;
      }
    };
};