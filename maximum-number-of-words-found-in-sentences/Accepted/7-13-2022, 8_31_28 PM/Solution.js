// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let max=0;
    for (let i of sentences){
        let count=1;
        for (let j of i){
            if (j==" "){
                count++;
            };
        };
        if(count > max){
            max = count;
        }

    };
    return max;

};