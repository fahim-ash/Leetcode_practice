// https://leetcode.com/problems/check-if-n-and-its-double-exist

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
    let list=arr.sort((a,b)=>b-a);
    for (let i of list){
        return i>0 && i%2==0;
        break
    }
        return false;
  
    
};