// https://leetcode.com/problems/find-all-duplicates-in-an-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let output=[];
    let list=[];
    for (let i of nums ){
        if (list[i]==i){
            output.push(i);
            
            }else{
              list[i]=i;  
            };
        
    };return output;
    
};