// https://leetcode.com/problems/find-smallest-letter-greater-than-target

/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let z=letters;
    z.push(target);
    z.sort();
    let idx=z.indexOf(target)
    console.log(z)
    return z[idx+1]
    
    
};