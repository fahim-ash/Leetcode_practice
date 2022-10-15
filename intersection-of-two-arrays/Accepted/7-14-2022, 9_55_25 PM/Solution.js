// https://leetcode.com/problems/intersection-of-two-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let list=[];
    let obj={};
    for(let i of nums1){
        for(let j of nums2){
            if(i==j){
                obj[i]=i
               
               };
        };
    };
    for (let i in obj ){
        list .push(i)
    };return list;
};