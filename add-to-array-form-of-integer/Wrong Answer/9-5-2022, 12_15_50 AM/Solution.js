// https://leetcode.com/problems/add-to-array-form-of-integer

/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let z=num.join("");
    let a=parseInt(z);
    console.log(a);
    let sum=a+k;
   
    sum = String(sum);
   
    return sum.split("")
    
};