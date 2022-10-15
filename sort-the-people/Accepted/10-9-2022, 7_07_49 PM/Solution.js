// https://leetcode.com/problems/sort-the-people

/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    let z=heights;
    let k=names
    for (let i in heights)
        for (let j in heights)
            if (z[j]<z[i]){
                let t=z[j];
                let x=k[j];
                z[j]=z[i];
                k[j]=k[i];
                z[i]=t;
                k[i]=x;
            
            
            
            }
    
    
    
    return k
                
        

    
    
    
};