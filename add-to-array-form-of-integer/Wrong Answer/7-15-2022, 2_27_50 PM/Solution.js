// https://leetcode.com/problems/add-to-array-form-of-integer

/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let z=num.join("");
    let a=parseInt(z);
    let sum=a+k;
    console.log(sum);
    sum = String(sum);
   
    return sum.split("")
    
  
 
    
};