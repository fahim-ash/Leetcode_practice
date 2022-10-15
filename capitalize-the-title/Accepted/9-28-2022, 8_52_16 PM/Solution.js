// https://leetcode.com/problems/capitalize-the-title

/**
 * @param {string} title
 * @return {string}
 */
var capitalizeTitle = function(title) {
    let word=title.split(" ");
    z="";
    for (let i of word){
        if (i.length>2){
            let m=i.charAt(0).toUpperCase();
            let res=m+i.slice(1).toLowerCase();
            z=z+res+" ";}
        else{
            z=z+i.toLowerCase()+" "
        }


    };
    return (z.substring(0,z.length-1));
    
};