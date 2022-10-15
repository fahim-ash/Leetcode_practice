// https://leetcode.com/problems/find-smallest-letter-greater-than-target

/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let z=[...new Set(letters)];
    if (!(z.includes(target)))
        z.push(target);
    z.sort();
    let idx=z.indexOf(target)
    console.log(z)
    if (z[idx+1]==null)
        return z[0]
    
    return z[idx+1]
    
    
};