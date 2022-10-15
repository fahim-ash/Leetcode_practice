// https://leetcode.com/problems/final-value-of-variable-after-performing-operations

/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let count=0;
    for (let i of operations ){
        if (i=='++X' || i=='X++'){
            count=count +1;
            }else{
                count =count-1;
            }
        
    }return count;
    
};