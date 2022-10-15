// https://leetcode.com/problems/majority-element

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let s={};
    for (let i of nums){
       
        if (!(i in s)){
            s[i]=1;
            
        }else{
            s[i]++;
        }
        
    }
    let max=0;
    let z=""
    for (let i in s){
        if (s[i]>max){
            max=s[i];
            z=i;
            
            }
        
        
    }
    return z;
};