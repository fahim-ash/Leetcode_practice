// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let list=[];
    for(let i =0;i<nums.length;i++){
        let count=0;
        
        for(let j =0;j<nums.length;j++){
            if (nums[i]>nums[j]){
                count=count+1;
               
                
            } 
            
        }list.push(count);
        
    }return list;
    
};